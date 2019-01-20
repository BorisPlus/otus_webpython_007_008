from django.contrib import admin
from . import models
from django.utils.html import mark_safe

from spices.admin_extra_classes import (
    ImageAdmin
)
from user_app import admin as user_app_admin

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


@admin.register(models.Lesson)
class LessonAdminModel(admin.ModelAdmin):
    list_per_page = 100
    inlines = (
        user_app_admin.SubscriptionInline,
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
