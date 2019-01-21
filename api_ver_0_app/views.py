from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth import (
    authenticate, login, logout
)
from django.shortcuts import get_object_or_404
from . import serializers
from dist_learn_app import models as dist_learn_app_models
from user_app import models as user_app_models
from rest_framework import status
from django.shortcuts import redirect


def get_default_view(request):
    return redirect('/rest_api/course/list')


class CourseList(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    queryset = dist_learn_app_models.Course.objects.all()


class CourseDetails(APIView):
    def get(self, request, *args, **kwargs):
        course_id = kwargs['pk']
        obj = dist_learn_app_models.Course.objects.get(pk=course_id)
        serializer = serializers.CourseDetailsSerializer(obj)
        return Response(serializer.data)


@permission_classes([IsAdminUser])
class LessonList(generics.ListAPIView):
    serializer_class = serializers.LessonDetailsSerializer
    queryset = dist_learn_app_models.Lesson.objects.all()


class LessonDetails(APIView):
    # TODO: переделать на generics CBV
    def get(self, request, *args, **kwargs):
        lesson_id = kwargs['pk']
        obj = dist_learn_app_models.Lesson.objects.get(pk=lesson_id)
        serializer = serializers.LessonDetailsSerializer(obj)
        return Response(serializer.data)


@permission_classes([AllowAny])
class CreateSubscriber(generics.CreateAPIView):
    serializer_class = serializers.SubscriberSerializer

    def post(self, request):
        user = request.data
        serializer = serializers.SubscriberSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
class LoginSubscriber(APIView):
    serializer_class = serializers.SubscriberSerializer

    def post(self, request):
        user = request.data
        authenticated_user = authenticate(username=user['username'], password=user['password'])
        if authenticated_user is not None and authenticated_user.is_active:
            login(request, authenticated_user)
            return Response({'username': user['username']}, status=status.HTTP_200_OK)

        if authenticated_user is not None and not authenticated_user.is_active:
            # user not is_active
            return Response({'username': user['username']}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({'username': user['username']}, status=status.HTTP_404_NOT_FOUND)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def current_subscriber(request, format=None):
    content = {
        'user': request.user.username if request.user else None,  # `django.contrib.auth.User` instance.
        'auth': request.auth.username if request.auth else None,  # None
    }
    return Response(content)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def logout_subscriber(request):
    # TODO: What is simple way to do JWT-logout, у меня поэтому тут SessionAuthentication
    username = request.user.username
    logout(request)
    return Response({'logout_subscriber': username})


@permission_classes([IsAuthenticated])
class SubscriberLessons(generics.ListAPIView):
    serializer_class = serializers.LessonDetailsSerializer

    def get_queryset(self):
        return dist_learn_app_models.Lesson.objects.filter(subscription__subscriber=self.request.user).all()


@permission_classes([IsAuthenticated])
class SubscriptionCheck(generics.ListAPIView):
    serializer_class = serializers.LessonIdentitySerializer

    def get_queryset(self):
        return dist_learn_app_models.Lesson.objects.filter(
            subscription__subscriber=self.request.user,
            pk=self.request.parser_context.get('kwargs', dict()).get('lesson_pk', 0)
        ).all()


@permission_classes([IsAuthenticated])
class SubscriptionChange(APIView):
    serializer_class = serializers.LessonIdentitySerializer

    def post(self, request, lesson_pk=0):
        lesson_id = lesson_pk
        try:
            lesson = get_object_or_404(dist_learn_app_models.Lesson, pk=lesson_id)
            subscription, was_created = user_app_models.Subscription.objects.get_or_create(
                subscriber=request.user,
                lesson=lesson
            )
            if not was_created:
                subscription.delete()
            data = {
                'subscriber': request.user.username,
                'subscriber_id': request.user.pk,
                'lesson_id': lesson_id,
                'value': 'was_unsubscribed' if not was_created else 'was_subscribed'
            }
            return Response(data, status=status.HTTP_200_OK)
        except dist_learn_app_models.Lesson.DoesNotExist:
            return Response({'lesson_id_is_invalid': lesson_id}, status=status.HTTP_404_NOT_FOUND)


@permission_classes([IsAdminUser])
class SubscriptionList(generics.ListAPIView):
    serializer_class = serializers.SubscriptionSerializer
    queryset = user_app_models.Subscription.objects.all()
