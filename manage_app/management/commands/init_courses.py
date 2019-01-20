from django.core.management.base import BaseCommand
from dist_learn_app import models
import os
import shutil

base_from_path = os.path.join(os.path.abspath('.'), 'manage_app', 'management', 'commands', 'courses_pics')
related_upload_path = os.path.join('static', 'uploads', 'test')
base_upload_path = os.path.join(os.path.abspath('.'), related_upload_path)
COURSES = [
    {
        'name': 'Гитара',
        'description': 'Научитесь уверенно аккомпонировать. Освоив ее, Вы освоите и любой другой инструмент.',
        'main_image': 'guitar.png'
    },

    {
        'name': 'Укуле́ле',
        'description': 'Очень простой и мелодичный инструмент.',
        'main_image': 'ukulele.png'
    },

    {
        'name': 'Дечиг по́ндар (по́ндур)',
        'description': 'Его звук весьма этнический, вибрирующий, звонкий.',
        'main_image': 'dechig_pondar.png'
    },

    {
        'name': 'Балалайка',
        'description': 'Русская душа',
        'main_image': 'balalayka.png'
    }
]


class Command(BaseCommand):
    help = 'Init courses'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        try:
            self.stdout.write(self.style.SUCCESS('Let\'s create courses:'))
            for course_index, course in enumerate(COURSES):

                course_object, was_group_create = models.Course.objects.get_or_create(
                    name=course['name']
                )
                course_object.description = course['description']
                course_object.order = course_index + 1
                from_path = os.path.join(base_from_path, course['main_image'])
                to_path = os.path.join(base_upload_path, course['main_image'])
                os.makedirs(base_upload_path, exist_ok=True)
                shutil.copyfile(from_path, to_path)
                course_object.main_image = os.path.join(related_upload_path, course['main_image'])
                course_object.save()

                self.stdout.write(
                    self.style.SUCCESS(
                        ' -> Course "%s" created with id "%s":' % (course['name'], course_object.id)))
            self.stdout.write(self.style.SUCCESS(' => All courses were created.'))

        except:
            raise
