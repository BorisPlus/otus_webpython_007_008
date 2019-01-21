from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from dist_learn_app import models as dist_learn_app_models
from user_app import models as user_app_models


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = dist_learn_app_models.Course
        fields = ('id', 'name', 'order', 'main_image', 'description')
        read_only_fields = ('id',)


class LessonIdentitySerializer(serializers.ModelSerializer):
    identity = serializers.CharField(write_only=True)

    class Meta:
        model = dist_learn_app_models.Lesson
        fields = ('id', 'identity')

    def get_identity(self, obj):
        return obj.pk


class LessonSerializer(LessonIdentitySerializer):
    class Meta:
        model = dist_learn_app_models.Lesson
        fields = tuple(list(LessonIdentitySerializer.Meta.fields) + ['date', 'name', 'description'])
        read_only_fields = ('id',)


class LessonDetailsSerializer(LessonSerializer):
    course = CourseSerializer(read_only=True)

    class Meta(LessonSerializer.Meta):
        fields = tuple(list(LessonSerializer.Meta.fields) + ['course'])


class CourseDetailsSerializer(CourseSerializer):
    lesson_set = LessonSerializer(many=True, read_only=True)

    class Meta(CourseSerializer.Meta):
        fields = tuple(list(CourseSerializer.Meta.fields) + ['lesson_set'])


class SubscriberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = user_app_models.Subscriber
        fields = ('username', 'password')

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class SubscriberSubscriptionsSerializer(SubscriberSerializer):
    lesson_set = LessonSerializer(many=True, read_only=True)

    class Meta(SubscriberSerializer.Meta):
        fields = tuple(list(CourseSerializer.Meta.fields) + ['lesson_set'])


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_app_models.Subscription
        fields = ('id', 'subscriber', 'lesson', 'date',)
        read_only_fields = ('id',)

    def to_representation(self, instance):
        self.fields['subscriber'] = SubscriberSerializer()
        self.fields['lesson'] = LessonDetailsSerializer()
        return super(SubscriptionSerializer, self).to_representation(instance)
