from .models import (
    Course,
)
from django.views.generic import (
    ListView,
    DetailView,
)

from django.shortcuts import redirect


def get_default_view(request):
    return redirect('/index')


class CourseList(ListView):
    model = Course
    template_name = 'dist_learn_app/courses/list.html'

    def get_queryset(self):
        queryset = super(CourseList, self).get_queryset()
        return queryset


class CourseLessons(DetailView):
    model = Course
    template_name = 'dist_learn_app/lessons/list.html'
