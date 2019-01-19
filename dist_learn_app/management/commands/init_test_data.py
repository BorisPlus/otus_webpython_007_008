from django.core.management.base import BaseCommand
from . import (
    init_users,
    init_courses,
    init_lessons
)


# manage.py create_users
class Command(BaseCommand):
    help = 'Init test database.'

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS('Let\'s init test database.'))
        self.stdout.write(self.style.SUCCESS(''))

        users = init_users.Command()
        users.handle(*args, **options)

        self.stdout.write(self.style.SUCCESS(''))

        courses = init_courses.Command()
        courses.handle(*args, **options)

        self.stdout.write(self.style.SUCCESS(''))

        lessons = init_lessons.Command()
        lessons.handle(*args, **options)

        self.stdout.write(self.style.SUCCESS(''))
        self.stdout.write(self.style.SUCCESS(' => Test database was init.'))
