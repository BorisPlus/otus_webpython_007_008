from rest_framework import serializers

from dist_learn_app import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'name', 'order', 'main_image', 'description')
        read_only_fields = ('id',)


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ('id', 'course', 'name', 'date', 'description',)
        read_only_fields = ('id',)

    def to_representation(self, instance):
        self.fields['course'] = CourseSerializer(read_only=True)
        return super(LessonSerializer, self).to_representation(instance)


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lesson
        fields = ('id', 'username',)
        read_only_fields = ('id',)


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subscription
        fields = ('id', 'subscriber', 'lesson', 'date',)
        read_only_fields = ('id',)

    def to_representation(self, instance):
        self.fields['subscriber'] = SubscriberSerializer()
        self.fields['lesson'] = LessonSerializer()
        return super(SubscriptionSerializer, self).to_representation(instance)

