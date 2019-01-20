from django.core.management.base import BaseCommand
from dist_learn_app import models

COURSE_LESSONS = [
    {
        'name': 'Гитара',
        'lessons': [
            {
                'name': 'Вступительный.',
                'date': '2019-02-01 00:00:00+0300',
                'description': 'История инструмента. Виды и настройка.',
            },
            {
                'name': 'Am,Dm,E - это наше ВСЁ.',
                'date': '2019-02-03 00:00:00+0300',
                'description': 'Базовые аккорды.',
            },
            {
                'name': 'Am,Dm,E - это НЕ наше всё..',
                'date': '2019-02-05 00:00:00+0300',
                'description': 'Продвинутые аккорды. Техника звукоизвлечения.',
            },
            {
                'name': 'Барэ.',
                'date': '2019-02-07 00:00:00+0300',
                'description': 'Барэ.',
            },
            {
                'name': 'Выпускной.',
                'date': '2019-02-09 00:00:00+0300',
                'description': 'Простая композиция.',
            }
        ]
    },
    {
        'name': 'Укуле́ле',
        'lessons': [
            {
                'name': 'Вступительный.',
                'date': '2019-02-01 12:00:00+0300',
                'description': 'История инструмента. Виды и настройка.',
            },
            {
                'name': 'Начинаем играть.',
                'date': '2019-02-03 12:00:00+0300',
                'description': 'Базовые аккорды.',
            },
            {
                'name': 'Под настроение.',
                'date': '2019-02-05 12:00:00+0300',
                'description': 'Мажор и минор.',
            },
            {
                'name': 'Выпускной.',
                'date': '2019-02-08 12:00:00+0300',
                'description': 'Простой рок-н-ролл.',
            }
        ]
    },
    {
        'name': 'Дечиг по́ндар (по́ндур)',
        'lessons': []
    },
    {
        'name': 'Балалайка',
        'lessons': []
    },
]


class Command(BaseCommand):
    help = 'Init lessons'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        try:
            self.stdout.write(self.style.SUCCESS('Let\'s create lessons:'))
            for course_index, course in enumerate(COURSE_LESSONS):

                self.stdout.write(
                    self.style.SUCCESS(
                        ' -> init course "%s"' % course['name']))
                course_object, was_group_create = models.Course.objects.get_or_create(
                    name=course['name']
                )
                for lesson in course['lessons']:
                    lesson_object, was_create = models.Lesson.objects.get_or_create(
                        name=lesson['name'],
                        description=lesson['description'],
                        date=lesson['date'],
                        course=course_object
                    )
                    self.stdout.write(
                        self.style.SUCCESS(
                            '   -> lesson "%s" created with id "%s":' % (lesson['name'], lesson_object.id)))
                self.stdout.write(
                    self.style.SUCCESS(
                        '   -> Course "%s" was init' % course['name']))
            self.stdout.write(self.style.SUCCESS(' => All lessons were created.'))

        except:
            raise
