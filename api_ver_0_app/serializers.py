from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from dist_learn_app import models as dist_learn_app_models
from user_app import models as user_app_models


class CourseSerializer(serializers.ModelSerializer):
    main_image = serializers.SerializerMethodField()

    class Meta:
        model = dist_learn_app_models.Course
        fields = ('id', 'name', 'order', 'main_image', 'description')
        read_only_fields = ('id',)

    def get_main_image(self, instance):
        """
        TODO: Мне бы хотелось иметь универсальный метод получения полного пути до картинки, независимо от
        отработавшего приложения

        Вариант:
        # request = self.context.get('request')
        # if not request:
        #     return '%s' % instance.main_image
        # return 'http://%s/%s' % (request.get_host(), instance.main_image)
        не совершенен по причине того, что request может быть None
        """
        return '%s' % instance.main_image


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
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = user_app_models.Subscriber
        fields = ('token', 'username', 'password')


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
