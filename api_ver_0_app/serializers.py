from rest_framework import serializers

from dist_learn_app import models


class CourseSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ('id', 'name', 'order', 'main_image', 'description')
        read_only_fields = ('id',)
        depth = 1

    def get_main_image(self, instance):
        # request = self.context.get('request')
        # if not request:
        #     return '%s' % instance.main_image
        # return 'http://%s/%s' % (request.get_host(), instance.main_image)
        return '%s' % instance.main_image


class LessonDetailsSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = models.Lesson
        fields = ('id', 'name', 'date', 'description', 'course')
        read_only_fields = ('id',)

        # def to_representation(self, instance):
        #     self.fields['course'] = CourseSerializer(read_only=True)
        #     return super(LessonSerializer, self).to_representation(instance)


class CourseLessonsSerializer(serializers.ModelSerializer):
    # main_image = serializers.SerializerMethodField()
    # lesson_set = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = models.Course
        fields = ('id', 'name', 'order', 'main_image', 'description')  # , 'lesson_set'
        read_only_fields = ('id',)

        # def to_representation(self, instance):
        # self.fields['lesson_set'] = LessonSerializer(read_only=True)
        # return super(CourseSerializer, self).to_representation(instance)

        # def get_main_image(self, instance):
        #     request = self.context.get('request')
        #     return 'http://%s/%s' % (request.get_host(), instance.main_image)


#
# class CourseSerializer(serializers.ModelSerializer):
#     # main_image = serializers.SerializerMethodField()
#     # lessons = serializers.RelatedField(many=True, read_only=True)
#
#     # lesson_set = serializers.StringRelatedField(many=True)
#     lesson_set = LessonSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = models.Course
#         fields = ('id', 'name', 'order', 'main_image', 'description', 'lesson_set')  #
#         read_only_fields = ('id',)
#         depth = 1
#
#     def to_representation(self, instance):
#         # self.fields['lesson_set'] = LessonSerializer(read_only=True)
#         return super(CourseSerializer, self).to_representation(instance)
#         # def get_main_image(self, instance):
#         #     request = self.context.get('request')
#         #     return 'http://%s/%s' % (request.get_host(), instance.main_image)


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
