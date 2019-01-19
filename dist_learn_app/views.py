from .models import (
    Course,
    Lesson,
    Subscriber,
    Subscription
)
from django.views.generic import (
    ListView,
    DetailView,
)
from django.views import (
    View,
)
from django.shortcuts import get_object_or_404

from django.http import (
    HttpResponseRedirect,
    JsonResponse,
)

from django.views.generic import TemplateView, RedirectView

from django.contrib.auth import (
    authenticate, login, logout
)


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

#
# from django.shortcuts import render, redirect
#
#
# class SubscriberLessons(View):
#     model = Subscriber
#     template_name = 'dist_learn_app/subscribers/lessons.html'
#
#     def get(self, request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             return get_default_view(request)
#
#         obj = self.model.objects.get(pk=request.user.id)
#         related = Subscription.objects.all().filter(subscriber=obj)
#         return render(request, self.template_name, {'object': obj, 'related': related})
#
#
# class SignInOrSignUp(TemplateView):
#     template_name = "dist_learn_app/auth/auth_form.html"
#
#     def post(self, request):
#
#         sign_in_error = None
#         sign_up_error = None
#         next_page = None
#
#         if request.POST.get('sign_in', False):
#             username = request.POST.get('sign_in_username', False)
#             password = request.POST.get('sign_in_password', False)
#             user = authenticate(username=username, password=password)
#             if user is not None and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(request.POST.get('next', '/'))
#
#             if user is not None and not user.is_active:
#                 sign_in_error = 'Пользователь не активирован'
#             else:
#                 sign_in_error = 'Неверный логин или пароль'
#
#             next_page = request.POST.get('next', '/')
#
#         if request.POST.get('sign_up', False):
#             username = request.POST.get('sign_up_username', False)
#             if Subscriber.objects.filter(username=username):
#                 context = self.get_context_data()
#                 context['sign_up_error'] = 'Пользователь с таким именем уже существует'
#                 context['next'] = request.POST.get('next', '/')
#                 return self.render_to_response(context)
#
#             password = request.POST.get('sign_up_password', False)
#             password_repiat = request.POST.get('sign_up_password_repiat', False)
#             if password != password_repiat:
#                 context = self.get_context_data()
#                 context['sign_up_error'] = 'Пароли не совпадают'
#                 context['next'] = request.POST.get('next', '/')
#                 return self.render_to_response(context)
#
#             Subscriber(username=username, password=password).save()
#             user = authenticate(username=username, password=password)
#             if user is not None and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(request.POST.get('next', '/'))
#
#             if user is not None and not user.is_active:
#                 sign_up_error = 'Пользователь не активирован'
#             else:
#                 sign_up_error = 'Что-то пошло не так'
#
#             next_page = request.POST.get('next', '/')
#
#         context = self.get_context_data()
#         context['next'] = next_page if next_page
#         context['sign_in_error'] = sign_in_error if sign_in_error
#         context['sign_up_error'] = sign_up_error if sign_up_error
#         return self.render_to_response(context)
#
#
# def sign_out(request):
#     logout(request)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#
#
# class ChangeSubscribe(View):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             lesson = get_object_or_404(Lesson, pk=kwargs.get('lesson_pk', 0))
#             subscription, was_created = Subscription.objects.get_or_create(
#                 subscriber=request.user,
#                 lesson=lesson
#             )
#             if not was_created:
#                 subscription.delete()
#             if request.is_ajax():
#                 data = {
#                     'value': 'was_unsubscribed' if not was_created else 'was_subscribed'
#                 }
#                 return JsonResponse({'ajax_response': data})
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
