from django.conf.urls import url
from . import views, user_views, apps
from django.views.generic import TemplateView


app_name = apps.DistLearnAppConfig.name

urlpatterns = [
    url(r'^index$', TemplateView.as_view(template_name="dist_learn_app/pages/index.html"), name="index"),
    url(r'^contacts$', TemplateView.as_view(template_name="dist_learn_app/pages/contacts.html"), name="contacts"),
    url(r'^course/list$', views.CourseList.as_view(), name="course_list"),
    url(r'^course/(?P<pk>\d+)/lessons$', views.CourseLessons.as_view(), name="course_lessons"),

    url(r'^login$', user_views.SignInOrSignUp.as_view(), name="login"),
    url(r'^logout$', user_views.sign_out, name="logout"),
    url(r'^subscriber/lessons$', user_views.SubscriberLessons.as_view(), name="subscriber_lessons"),
    url(r'^lesson/(?P<lesson_pk>\d+)/subscribe/change$', user_views.ChangeSubscribe.as_view(), name="change_subscribe"),

    url(r'', views.get_default_view, name="default")
]
