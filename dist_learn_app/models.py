from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Он должен быть связан с фронтовой частью, которую делали с Юрой,
# желательно в одном репозитории.
# То есть, как на отусе: у нас есть курс, у которого есть занятия,
# у курсов есть преподаватели, а ещё пользователи, которые могут
# зарегистрироваться и залогиниться.
# То есть должны быть следующие возможности:
#  - зарегистрироваться, можно без капчи и подтверждения email;
#  - залогиниться; - посмотреть список курсов;
#  - зайти внутрь одного курса, где посмотреть его описание и список уроков, прикриплённых к дате;
#  - дополнительно можно задать возможность записаться на курс.
# Делается с помощью CBV и использования фишичек, про которые рассказывал о django Илья.
# Возможно, он добавлял ещё что-то, что нужно сделать. Но основная база всё равно будет указанная выше :)


import datetime

import uuid


def get_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'static/uploads/%s/%s/%s.jpg' % (filename[:1], filename[2:3], filename)


class Course(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('order',)
        unique_together = (('name',),)

    name = models.CharField(blank=False, null=False, max_length=50, verbose_name='Название курса', )
    order = models.PositiveIntegerField(blank=False, null=False, default=1, verbose_name='#', )
    main_image = models.FileField(blank=False, null=False, default='undef.png',
                                  verbose_name='Иконка курса',
                                  upload_to=get_upload_path)

    description = models.TextField(blank=True, null=True, max_length=250, verbose_name='Описание курса', )

    def __str__(self):
        return '{name}'.format(name=self.name)


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('-date', 'name',)
        unique_together = (('name', 'course'),)

    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name=Course._meta.verbose_name.title())

    name = models.CharField(blank=False, null=False, max_length=50, verbose_name='Наименование урока', )
    date = models.DateTimeField(blank=False, null=False, default=datetime.datetime.now,
                                verbose_name='Дата и время проведения урока')
    description = models.TextField(blank=True, null=True, max_length=250, verbose_name='Описание урока', )

    def __str__(self):
        return '{name}'.format(name=self.name)


class SubscriberManager(models.Manager):
    def get_queryset(self):
        return super(SubscriberManager, self).get_queryset().filter(is_superuser=False)

    # Django > 1.11 требует реализации данного метода при расширении стандартной модели
    # пользователей административной части
    def normalize_email(cls, email):
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])

        return email


class Subscriber(User):
    objects = SubscriberManager()

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
        proxy = True
        ordering = ('last_name', 'first_name', 'username')

    def __init__(self, *args, **kwargs):
        self._meta.get_field('is_staff').default = False
        super(Subscriber, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(Subscriber, self).save(*args, **kwargs)

    def __str__(self):
        return '%s (%s %s)' % (
            self.username,
            self.last_name if self.last_name else 'н.д.',
            self.first_name if self.first_name else 'н.д.',
        )


class Subscription(models.Model):
    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = (('subscriber', 'lesson'),)
        ordering = ('-lesson__date', '-lesson', 'subscriber')

    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE,
                                   verbose_name=Subscriber._meta.verbose_name.title())
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                               verbose_name=Lesson._meta.verbose_name.title())
    date = models.DateField(blank=False, null=False, auto_now=True, verbose_name='дата подписи')

    def __str__(self):
        return '{subscriber} ()<--= {lesson}'.format(
            subscriber=self.subscriber,
            lesson=self.lesson
        )
