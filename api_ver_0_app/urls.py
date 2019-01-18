from . import views

from django.urls import path
urlpatterns = [
    path('course/list', views.CourseList.as_view()),
    path('course/<int:pk>', views.Course.as_view()),
    path('course/<int:pk>/lesson/list', views.LessonList.as_view()),
    path('', views.CourseList.as_view())
]
