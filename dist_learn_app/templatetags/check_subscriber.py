from django import template

register = template.Library()


@register.filter(name='check_subscription_exists')
def check_subscription_exists(value, lesson):
    if not value:
        return False
    return lesson.subscription_set.filter(subscriber=value).exists()
