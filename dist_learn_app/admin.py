from django.contrib import admin
from . import models
from django.utils.html import mark_safe

from spices.admin_extra_classes import (
    ImageAdmin
)

admin.site.site_header = 'Открытые уроки'


class LessonInline(admin.TabularInline):
    model = models.Lesson
    extra = 1


@admin.register(models.Course)
class CourseAdminModel(ImageAdmin):
    inlines = (
        LessonInline,
    )
    image_fields = [
        'main_image',
    ]
    list_per_page = 100
    fields = [
        'name',
        'order',
        'main_image',
        'description',
    ]
    list_display = (
        'name',
        'order',
        'get_main_image',
        'description',
    )
    search_fields = [
        'name',
        'description'
    ]

    def get_main_image(self, obj):
        return mark_safe("<img width='50px' src='/{v}' alt='{v}' />".format(v=obj.main_image))

    get_main_image.short_description = models.Course._meta.get_field('main_image').verbose_name
    get_main_image.admin_order_field = 'main_image'


class SubscriptionInline(admin.TabularInline):
    model = models.Subscription
    extra = 1


@admin.register(models.Lesson)
class LessonAdminModel(admin.ModelAdmin):
    list_per_page = 100
    inlines = (
        SubscriptionInline,
    )
    fields = [
        'date',
        'name',
        'description',
    ]
    list_display = (
        'course',
        'date',
        'name',
        'description',
    )
    search_fields = [
        'course__name',
        'name',
        'description'
    ]


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

    get_lesson_date.short_description = models.Lesson._meta.get_field('name').verbose_name
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
