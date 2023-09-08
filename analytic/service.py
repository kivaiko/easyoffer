import requests
import json
import re
import bleach
from collections import Counter
from .word_filter import words_filter
from easyoffer.settings import HEADERS
from .models import Search


search_url = 'https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=NAME%3A%28%21%22flask%22%29+and+DESCRIPTION%3A%28%21%22flask%22%29&ored_clusters=true&enable_snippets=true&L_save_area=true'
# search_python = Search.objects.all(id=2)


def get_link(url):
    print('Start – get_link')
    url = url[29:]
    search_link = f'https://api.hh.ru/vacancies?{url}&per_page=100'
    return search_link


def get_vacancies_id(url):
    print('Start – get_vacancies_id')
    vacancies_ids = []
    response = requests.get(url, headers=HEADERS)
    data = json.loads(response.text)
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
    return skills_list, keywords_list


def clean(txt):
    all_words = []
    for word in txt.split():
        all_words.append(word)
    new_list = [item for item in all_words if item not in words_filter]
    return new_list


def count_words(url):
    link = get_link(url)
    vacancies_ids = get_vacancies_id(link)
    skills, keywords = get_data_from_vacancies_id(vacancies_ids)
    print(Counter(skills).most_common(50))
    print(' ')
    print(Counter(keywords).most_common(50))


# print(search_python)
