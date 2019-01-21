from django.conf import settings


def template_media(request):
    return {'MEDIA_PATH': "/%s" % settings.MEDIA_DIR_NAME}
