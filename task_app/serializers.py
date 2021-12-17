from rest_framework import serializers

from . import models, constances, error_messages
from typing import List


class Serializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super(Serializer, self).__init__(*args, **kwargs)
        for field in self.fields:
            for error in error_messages.errors:
                self.fields[field].error_messages[error] = error_messages.errors[error]


class ModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(ModelSerializer, self).__init__(*args, **kwargs)
        for field in self.fields:
            for error in error_messages.errors:
                self.fields[field].error_messages[error] = error_messages.errors[error]


class AnswerSerializer(Serializer):
    id = serializers.IntegerField(allow_null=False, required=True)
    text = serializers.CharField(allow_null=False, allow_blank=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class QuestionSerializer(ModelSerializer):
    next_id = serializers.SerializerMethodField("get_next_id", allow_null=True)
    answers = AnswerSerializer(many=True,allow_null=False)
    # answers = serializers.SerializerMethodField("get_answers", allow_null=False)

    class Meta:
        model = models.Question
        fields = ["id", "text", "next_id", "answers"]
        read_only_fields = ["id", "text", "answers", "next_id"]



    def get_next_id(self, attr) -> int:
        objects = models.Question.objects.order_by("order_index")
        index = list(objects).index(self.instance)

        if index == len(objects) - 1:
            return None
        else:
            return objects[index + 1].id


class IsExistParticipantSerializer(Serializer):
    is_exist = serializers.BooleanField(default=False, allow_null=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GetHealthQuestionSerializer(Serializer):
    get_covid_19 = serializers.CharField()
    get_drug = serializers.CharField()
    mental_disorder = serializers.CharField(allow_null=False, allow_blank=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class TermSerializer(Serializer):
    text = serializers.CharField(allow_null=False, allow_blank=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class HowDoTaskSerializer(Serializer):
    text = serializers.CharField(allow_null=False, allow_blank=False)
    gif = serializers.CharField(allow_null=False, allow_blank=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class TaskImageSerializer(ModelSerializer):
    class Meta:
        model = models.Image
        fields = ["id", "picture"]
        read_only_fields = ["id", "picture"]


class ParticipantSerializer(ModelSerializer):
    class Meta:
        model = models.Participant
        fields = ["name", "family_name", "birth_year", "education_level", "mobile_number", "gender"]


class HealthSerializer(ModelSerializer):
    class Meta:
        model = models.Health
        fields = ["get_covid_19", "get_drug", "mental_disorder"]


class ParticipantQuestionAnswerSerializer(ModelSerializer):
    class Meta:
        model = models.ParticipantQuestionAnswer
        fields = ["question", "answer"]


class TaskRegisterSerializer(Serializer):
    participant = ParticipantSerializer(allow_null=False, required=True)
    health = HealthSerializer(allow_null=False, required=True)
    answers = ParticipantQuestionAnswerSerializer(many=True, allow_null=False, required=True)

    @staticmethod
    def validate_answers(answers):
        if len(answers) != models.Question.objects.count():
            raise serializers.ValidationError("تعداد سوالات پاسخ داده درست نمیباشد.")

        return answers

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        participant = ParticipantSerializer().create(validated_data["participant"])
        health_data = validated_data["health"]
        health_data["participant"] = participant
        health = HealthSerializer().create(health_data)
        answers = []
        for answer in validated_data["answers"]:
            participant_question_answer_data = answer
            participant_question_answer_data["participant"] = participant
            answers.append(ParticipantQuestionAnswerSerializer().create(participant_question_answer_data))
        return {
            "participant": participant,
            "health": health,
            "answers": answers
        }


class TaskInfoSerializer(Serializer):
    images = TaskImageSerializer(many=True, allow_null=False)
    orders = serializers.ListField(child=serializers.IntegerField(allow_null=False), allow_null=False,
                                   allow_empty=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
