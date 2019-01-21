from django.contrib import admin
from . import models
from dist_learn_app import models as dist_learn_app_models

admin.site.site_header = 'Пользователи'


class SubscriptionInline(admin.TabularInline):
    model = models.Subscription
    extra = 1


@admin.register(models.Subscription)
class SubscriptionAdminModel(admin.ModelAdmin):
    list_per_page = 100
    fields = [
        'lesson',
        'subscriber',
        'date',
    ]
    list_display = (
        'get_lesson_date',
        'lesson',
        'subscriber',
        'date',
    )
    search_fields = [
        'lesson',
        'subscriber'
    ]

    def get_lesson_date(self, obj):
        return obj.lesson.date

    get_lesson_date.short_description = dist_learn_app_models.Lesson._meta.get_field('name').verbose_name
    get_lesson_date.admin_order_field = 'lesson__date'


@admin.register(models.Subscriber)
class SubscriberAdminModel(admin.ModelAdmin):
    inlines = (
        SubscriptionInline,
    )
    list_per_page = 100
    fields = [
        'username',
        'first_name',
        'last_name',
    ]
    list_display = (
        'username',
        'first_name',
        'last_name',
        'date_joined',
    )
    search_fields = [
        'username',
        'first_name',
        'last_name',
    ]
