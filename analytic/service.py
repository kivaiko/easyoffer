import requests
import json
import re
import bleach
from collections import Counter

from rating.models import Profession
from .word_filter import words_filter
from easyoffer.settings import HEADERS
from .models import Search, Skill, KeyWord
from datetime import datetime


def get_link(url):
    print('Start – get_link')
    url = url[29:]
    search_link = f'https://api.hh.ru/vacancies?{url}&per_page=100'
    return search_link


def get_vacancies_id(url, search):
    print('Start – get_vacancies_id')
    vacancies_ids = []
    response = requests.get(url, headers=HEADERS)
    data = json.loads(response.text)
    search.amount_vacancies = data['found']
    search.last_update = datetime.now()
    search.save()
    print(search.amount_vacancies)
    print(search.last_update)
    pages = data['pages']
    for page in range(pages):
        response = requests.get(url, headers=HEADERS, params={'page': page})
        data = json.loads(response.text)
        clear_data = data['items']
        for i in clear_data:
            vacancies_ids.append(i['id'])
    return vacancies_ids


def get_skills_from_id(data):
    skills_for_id = []
    for skill in data:
        skills_for_id.append(skill['name'])
    return skills_for_id


def get_keywords_from_id(data):
    vacancies_description = ''
    txt = bleach.clean(data, tags=[], strip=True)
    txt = re.findall(r'[A-Za-z0-9]+', txt)
    txt = ' '.join(txt)
    txt = txt.lower()
    vacancies_description += txt
    words_list = clean(vacancies_description)
    return words_list


def get_data_from_vacancies_id(ids):
    print('Start – get_data_from_vacancies_id')
    skills_list = []
    keywords_list = []
    for vacancy_id in ids:
        print(vacancy_id)
        response = requests.get('https://api.hh.ru/vacancies/' + vacancy_id, headers=HEADERS)
        data = json.loads(response.text)
        skills_list += get_skills_from_id(data['key_skills'])
        keywords_list += get_keywords_from_id(data['description'])
        skills_sorted = Counter(skills_list).most_common(100)
        keywords_sorted = Counter(keywords_list).most_common(100)
    return skills_sorted, keywords_sorted


def clean(txt):
    all_words = []
    for word in txt.split():
        all_words.append(word)
    new_list = [item for item in all_words if item not in words_filter]
    return new_list


def add_skills_to_db(skills, search):
    Skill.objects.filter(search_id=search.id).delete()
    for skill in skills:
        Skill.objects.create(
            title=skill[0],
            amount=skill[1],
            search_id=search.id
        )


def add_keywords_to_db(keywords, search):
    KeyWord.objects.filter(search_id=search.id).delete()
    for keyword in keywords:
        KeyWord.objects.create(
            title=keyword[0],
            amount=keyword[1],
            search_id=search.id
        )


def count_words():
    print('count_words – запущена')
    searches_queryset = Search.objects.all().filter(public=True)
    print(f'Queryset: {searches_queryset}')
    for search in searches_queryset:
        try:
            print(f'Обработка {search} – запущена')
            link = get_link(search.url)
            vacancies_ids = get_vacancies_id(link, search)
            skills, keywords = get_data_from_vacancies_id(vacancies_ids)
            print(f'Данные для {search} – Собраны')
            add_skills_to_db(skills, search)
            print(f'Скилы для {search} – Добавлены в базу')
            add_keywords_to_db(keywords, search)
            print(f'Ключевые для {search} – Добавлены в базу')
        except:
            continue


def get_search_data(request, slug):
    title = request.GET.get("title")
    prof_data = Profession.objects.get(slug=slug)
    searches_for_prof = Search.objects.filter(profession=prof_data)
    if title:
        search = Search.objects.get(profession=prof_data, title=title)
    else:
        search = Search.objects.get(profession=prof_data, title='Все')
    skills = Skill.objects.filter(search=search).order_by('-amount')
    keywords = KeyWord.objects.filter(search=search).order_by('-amount')
    return search, skills, keywords, searches_for_prof
