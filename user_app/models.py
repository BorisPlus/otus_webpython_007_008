from django.db import models
from dist_learn_app import models as dist_learn_app_models
from django.contrib.auth.models import User


class SubscriberManager(models.Manager):
    def get_queryset(self):
        # TODO: надо подумать над ".filter(is_superuser=False)"
        return super(SubscriberManager, self).get_queryset()

    # Django > 1.11 требует реализации данного метода при расширении стандартной модели
    # пользователей административной части
    def normalize_email(cls, email):
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError as value_exc:
            raise value_exc
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
        return self.username


class Subscription(models.Model):
    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        unique_together = (('subscriber', 'lesson'),)
        ordering = ('-lesson__date', '-lesson', 'subscriber')

    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE,
                                   verbose_name=Subscriber._meta.verbose_name.title())
    lesson = models.ForeignKey(dist_learn_app_models.Lesson, on_delete=models.CASCADE,
                               verbose_name=dist_learn_app_models.Lesson._meta.verbose_name.title())
    date = models.DateField(blank=False, null=False, auto_now=True, verbose_name='дата подписи')

    def __str__(self):
        return '{subscriber} ()<--= {lesson}'.format(
            subscriber=self.subscriber,
            lesson=self.lesson
        )
