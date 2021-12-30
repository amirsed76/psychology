from django.shortcuts import render
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from . import serializers, models, constances, image_orders, utils
import random
from rest_framework.views import APIView


class QuestionRetrievedAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.QuestionSerializer
    queryset = models.Question.objects.all()

    def get_object(self):
        answers = [{"id": key, "text": value} for key, value in constances.ANSWERS.items()]
        if "pk" not in self.kwargs:
            obj = self.queryset.order_by("order_index").first()
        else:
            obj = super(QuestionRetrievedAPIView, self).get_object()
        obj.answers = answers
        return obj


class ExistParticipant(generics.RetrieveAPIView):
    queryset = models.Participant.objects.all()
    lookup_field = "mobile_number"
    serializer_class = serializers.IsExistParticipantSerializer

    def get_object(self):
        participant = None
        task_date = None
        try:
            participant = super(ExistParticipant, self).get_object()
            task_date = utils.get_task_date(participant=participant)
            is_exist = True

            if participant.health is None:
                is_exist = False
            elif participant.participantquestionanswer_set.count() < models.Question.objects.count():
                is_exist = False

        except Exception as e:
            is_exist = False

        if not is_exist and participant is not None:
            participant.delete()
        return {"is_exist": is_exist, "task_date": task_date}


class GetHealthQuestionAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.GetHealthQuestionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = constances.HELTH_QUESTIONS
        serializer = self.serializer_class(instance)
        return Response(serializer.data)


class GetTermAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.TermSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = {"text": constances.TERM}
        serializer = self.serializer_class(instance)
        return Response(serializer.data)


class GetQuestionTextAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.TermSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = {"text": constances.QUESTION_TEXT}
        serializer = self.serializer_class(instance)
        return Response(serializer.data)


class GetHowDoTaskAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.HowDoTaskSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = {
            "text": constances.HOW_DO_TASK["text"],
            "gif": self.request.build_absolute_uri(constances.HOW_DO_TASK["gif"])
        }
        serializer = self.serializer_class(instance)
        return Response(serializer.data)


class TaskRegisterCreateAPIView(generics.CreateAPIView):
    queryset = models.Participant.objects.all()
    serializer_class = serializers.TaskRegisterSerializer


class TaskTrainingInitInfoAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.TaskInfoSerializer

    def retrieve(self, request, *args, **kwargs):
        qs = models.Image.objects.all()  # TODO  select for all categories
        images = random.sample(list(qs), k=5)
        images_by_repeat = images + random.choices(images, k=5)
        random.shuffle(images_by_repeat)
        orders = [image.id for image in images_by_repeat]
        serializer = self.get_serializer(instance={"images": images, "orders": orders})

        return Response(serializer.data)


class TaskInitInfoAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.TaskInfoSerializer

    def retrieve(self, request, *args, **kwargs):
        qs = models.Image.objects.all()
        images = random.sample(list(qs), k=25)
        orders = image_orders.make_order(order=image_orders.get_random_order(), ids=[image.id for image in images])
        serializer = self.get_serializer(instance={"images": images, "orders": orders})

        return Response(serializer.data)


class ApplyTaskCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ApplyTaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
