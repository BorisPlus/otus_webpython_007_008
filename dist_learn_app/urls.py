from django.conf.urls import url
from . import views, apps
from django.views.generic import TemplateView


app_name = apps.DistLearnAppConfig.name

urlpatterns = [
    url(r'^index$', TemplateView.as_view(template_name="templates_app/pages/index.html"), name="index"),
    url(r'^contacts$', TemplateView.as_view(template_name="templates_app/pages/contacts.html"), name="contacts"),
    url(r'^course/list$', views.CourseList.as_view(), name="course_list"),
    url(r'^course/(?P<pk>\d+)/lessons$', views.CourseLessons.as_view(), name="course_lessons"),

    url(r'', views.get_default_view, name="default")
]
