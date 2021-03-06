import datetime

from rest_framework import serializers

from . import models, constances, error_messages, utils
from typing import List
import math


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
    answers = AnswerSerializer(many=True, allow_null=False)

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
    task_date = serializers.DateField(allow_null=False)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GetHealthQuestionSerializer(Serializer):
    get_covid_19 = serializers.CharField()
    get_drug = serializers.CharField()
    mental_disorder = serializers.CharField(allow_null=False, allow_blank=False)
    get_medicine = serializers.CharField()

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
    mobile_number = serializers.CharField(min_length=11, max_length=11)

    class Meta:
        model = models.Participant
        fields = ["name", "family_name", "birth_year", "education_level", "mobile_number", "gender"]

    @staticmethod
    def validate_mobile_number(mobile_number):
        english_digits = utils.convert_digit(mobile_number)
        return english_digits


class HealthSerializer(ModelSerializer):
    class Meta:
        model = models.Health
        fields = ["get_covid_19", "get_drug", "mental_disorder", "get_medicine"]


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
            raise serializers.ValidationError("?????????? ???????????? ???????? ???????? ???????? ??????????????.")

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


class ReactionTimeSerializer(ModelSerializer):
    class Meta:
        model = models.TaskEventImageReactionTime
        fields = ["image", "reaction_time"]


class ApplyTaskSerializer(ModelSerializer):
    reaction_times = ReactionTimeSerializer(many=True, write_only=True, allow_null=False)
    mobile_number = serializers.CharField(write_only=True, allow_null=False, allow_blank=False)
    next_date = serializers.SerializerMethodField(method_name="get_next_date", read_only=True, allow_null=False)
    score = serializers.SerializerMethodField(method_name="get_score", read_only=True, allow_null=False)
    reaction_time_mean = serializers.SerializerMethodField(method_name="get_reaction_time_mean", read_only=True,
                                                           allow_null=False)
    text = serializers.SerializerMethodField(method_name="get_text", read_only=TaskRegisterSerializer, allow_null=False)

    class Meta:
        model = models.TaskEvent
        fields = ["mobile_number", "reaction_times", "next_date", "score", "reaction_time_mean", "text"]

    @staticmethod
    def validate_mobile_number(mobile_number):
        mobile_number = utils.convert_digit(mobile_number)
        if not models.Participant.objects.filter(mobile_number=mobile_number).exists():
            raise serializers.ValidationError("?????? ?????????? ?????????? ??????????????.")

        return mobile_number

    def validate(self, attrs):
        participant = models.Participant.objects.get(mobile_number=attrs.pop("mobile_number"))
        attrs["participant"] = participant
        if not utils.can_do_task(participant=participant):
            raise serializers.ValidationError("???????? ?????????? ???????????? ?? ?????? ???????????? ??????.")

        return attrs

    @staticmethod
    def validate_reaction_times(reaction_times):
        if len(reaction_times) != 50:
            raise serializers.ValidationError("?????????? ???????? ?????? ?????????? ?????? ???????? ??????????????.")
        return reaction_times

    def create(self, validated_data):
        reaction_times = validated_data.pop("reaction_times")
        event = super(ApplyTaskSerializer, self).create(validated_data)
        for reaction_time in reaction_times:
            reaction_time["task_event"] = event
            ReactionTimeSerializer().create(reaction_time)

        return event

    @staticmethod
    def get_next_date(event: models.TaskEvent) -> datetime.date:
        return event.get_next_date()

    @staticmethod
    def get_score(event: models.TaskEvent) -> int:
        return event.get_score()

    @staticmethod
    def get_reaction_time_mean(event: models.TaskEvent) -> int:
        return event.get_reaction_time_mean()

    @staticmethod
    def get_questions_score(event):
        return event.participant.get_questions_score()

    def get_text(self, event):
        return constances.APPRECIATION + f"\n\n\n  ????????????? ?????? ?????? ???? ????????????? ???????????? ??????: {self.get_questions_score(event)}"
