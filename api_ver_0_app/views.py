from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly
from rest_framework.views import APIView
# from rest_framework import status
from . import serializers
from dist_learn_app import models


@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([DjangoModelPermissionsOrAnonReadOnly])
class CourseList(generics.ListAPIView):
    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()


@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([DjangoModelPermissionsOrAnonReadOnly])
class Course(APIView):
    def get(self, request, *args, **kwargs):
        course_id = kwargs['course_id']
        obj = models.Course.objects.get(pk=course_id)
        serializer = serializers.CourseSerializer(obj)
        return Response(serializer.data)


@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([DjangoModelPermissionsOrAnonReadOnly])
class LessonList(generics.ListAPIView):
    serializer_class = serializers.LessonSerializer

    def get(self, *args, **kwargs):
        serializer = serializers.LessonSerializer(
            models.Course.objects.all()
        )
        return Response(serializer.data)
