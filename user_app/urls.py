from django.conf.urls import url
from . import views, apps


app_name = apps.UserAppConfig.name

urlpatterns = [

    url(r'^login$', views.SignInOrSignUp.as_view(), name="login"),
    url(r'^logout$', views.sign_out, name="logout"),
    url(r'^lessons$', views.SubscriberLessons.as_view(), name="subscriber_lessons"),
    url(r'^lesson/(?P<lesson_pk>\d+)/subscribe/change$', views.ChangeSubscribe.as_view(), name="change_subscribe"),
]
