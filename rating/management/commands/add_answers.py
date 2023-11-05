import os
import openai
from django.db.models import Count, Q
from rating.models import Rating, Answer, Profession
from django.core.management.base import BaseCommand, CommandError

openai.api_key = os.environ.get('OPENAPI_KEY')


class Command(BaseCommand):
    help = 'Добавляет ответы на неотвеченные вопросы'

    def add_arguments(self, parser):
        parser.add_argument('profession_id', type=int, help='ID профессии для которой будут добавлены ответы')
        parser.add_argument('questions_qty', type=int, help='Количество вопросов, на которые нужно добавить ответы')
        parser.add_argument('gpt_model', type=str, help='Название модели GPT для генерации ответов')

    def generate_response(self, question, gpt_model, prof_title):
        prompt = f"{question}"
        response = openai.ChatCompletion.create(
            model=gpt_model,
            messages=[
                {"role": "system", "content": f"Вы {prof_title} на техническом собеседовании, сформируй ответ в html"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700,
            n=1
        )
        return response.choices[0].message.content if response.choices else "Нет ответа."

    def get_unanswered_questions(self, profession_id, questions_qty):
        ratings_with_questions = Rating.objects.filter(
            profession_id=profession_id,
            public=True
        ).exclude(
            question__answer__public=False
        ).annotate(
            num_answers=Count('question__answer', filter=Q(question__answer__public=True))
        ).filter(
            num_answers=0
        ).order_by('-rating').values('id', 'question__title')[:questions_qty]

        return {item['id']: item['question__title'] for item in ratings_with_questions}

    def handle(self, *args, **options):
        profession_id = options['profession_id']
        questions_qty = options['questions_qty']
        gpt_model = options['gpt_model']

        try:
            prof_title = Profession.objects.get(id=profession_id).title
            ratings_id_with_question_title = self.get_unanswered_questions(profession_id, questions_qty)

            for rating_id, question_title in ratings_id_with_question_title.items():
                answer_text = self.generate_response(question_title, gpt_model, prof_title)
                Answer.objects.create(
                    question_id=rating_id,
                    text=answer_text,
                    author=gpt_model,
                    public=True
                )
                self.stdout.write(self.style.SUCCESS(f'Ответ на вопрос "{question_title}" успешно добавлен.'))

            self.stdout.write(self.style.SUCCESS(f'Всего успешно добавлено {len(ratings_id_with_question_title)} ответов для профессии {prof_title}.'))

        except Profession.DoesNotExist:
            raise CommandError('Профессия с указанным ID не найдена')
        except Exception as e:
            raise CommandError(f'Произошла ошибка при добавлении ответов: {str(e)}')
