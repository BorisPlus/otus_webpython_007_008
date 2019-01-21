from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    # open
    path('course/list', views.CourseList.as_view(), name="api_course_list"),
    path('course/<int:pk>', views.CourseDetails.as_view(), name="api_course_details"),
    path('lesson/<int:pk>', views.LessonDetails.as_view(), name="api_lesson_details"),

    # auth need
    path('subscriber/create', views.CreateSubscriber.as_view(), name="api_subscriber_create"),
    path('subscriber/login', views.LoginSubscriber.as_view(), name="api_subscriber_login"),
    path('subscriber/current', views.current_subscriber, name="api_subscriber_current"),
    path('subscriber/logout', views.logout_subscriber, name="api_subscriber_logout"),
    path('subscriber/lesson/list', views.SubscriberLessons.as_view(), name="api_subscriber_lesson_list"),
    path('lesson/<int:lesson_pk>/subscription/check', views.SubscriptionCheck.as_view(), name="api_subscription_check"),
    path('lesson/<int:lesson_pk>/subscription/change', views.SubscriptionChange.as_view(),
         name="api_subscription_change"),

    # admin only
    path('subscription/list', views.SubscriptionList.as_view(), name="api_subscription_list"),
    path('lesson/list', views.LessonList.as_view(), name="api_lesson_list"),

    # reach url need
    url(r'', views.get_default_view, name="api_default")
]
