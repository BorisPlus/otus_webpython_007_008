from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^index$', TemplateView.as_view(template_name="dist_learn_app/pages/index.html"), name="index"),
    url(r'^contacts$', TemplateView.as_view(template_name="dist_learn_app/pages/contacts.html"), name="contacts"),
    url(r'^login$', views.SignInOrSignUp.as_view(), name="sign_in"),
    url(r'^logout$', views.sign_out, name="logout"),
    url(r'^course/list$', views.CourseList.as_view(), name="course_list"),
    url(r'^course/(?P<pk>\d+)/lessons$', views.CourseLessons.as_view(), name="course_lessons"),
    url(r'^lesson/(?P<lesson_pk>\d+)/subscribe/change$', views.ChangeSubscribe.as_view(), name="change_subscribe"),
    url(r'', views.CourseList.as_view(template_name="dist_learn_app/pages/index.html"), name="default")
]
