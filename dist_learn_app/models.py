from django.db import models

import datetime

import uuid
import os


def get_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('static', 'uploads', filename[:1], filename[2:3], '%s.jpg' % filename )


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
        return self.name


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
        return self.name

