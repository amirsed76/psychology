from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from django.core.validators import MaxValueValidator, MinValueValidator


class ModelSer():
    def __init__(self):
        # Run through all error messages provided in the Meta class and update
        for field_name, err_dict in self.opts.error_messages.iteritems():
            self.fields[field_name].error_messages.update(err_dict)


class Participant(models.Model):
    Gender = [
        ("male", "male"),
        ("female", "female")
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    family_name = models.CharField(max_length=100, null=False, blank=False)
    birth_year = models.IntegerField(null=False, blank=False, validators=[
        MaxValueValidator(1410),
        MinValueValidator(1270)
    ],default=1320)
    education_level = models.PositiveSmallIntegerField(null=False, blank=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    mobile_number = models.CharField(max_length=11, validators=[
        RegexValidator('^09[0-9]{9}$', message='شماره ی موبایل معتبر نمیباشد.')], null=False, blank=False, unique=True)
    gender = models.CharField(max_length=6, choices=Gender, null=False, blank=False)

    def __str__(self):
        return f"{self.name} {self.family_name} {self.mobile_number}"


class Health(models.Model):
    participant = models.OneToOneField("Participant", null=False, blank=False, on_delete=models.CASCADE)
    get_covid_19 = models.PositiveSmallIntegerField(null=False, blank=False, validators=[
        MaxValueValidator(2),
        MinValueValidator(0)
    ])
    get_drug = models.BooleanField(null=False, blank=False)
    mental_disorder = models.TextField(null=False, blank=True)

    def __str__(self):
        return f"{self.participant}"


class Question(models.Model):
    text = models.TextField(null=False, blank=False, unique=True)
    order_index = models.PositiveSmallIntegerField(null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.order_index}.{self.text}"


class ParticipantQuestionAnswer(models.Model):
    participant = models.ForeignKey("Participant", null=False, blank=False, on_delete=models.CASCADE)
    question = models.ForeignKey("Question", null=False, blank=False, on_delete=models.CASCADE)
    answer = models.PositiveSmallIntegerField(null=False, blank=False, validators=[
        MaxValueValidator(9),
        MinValueValidator(1)
    ], default=1)

    class Meta:
        unique_together = [['participant', "question"]]

    def __str__(self):
        return f"{self.participant.id} => {self.question}: {self.answer}"


class Image(models.Model):
    CATEGORY = [
        (1, "Building"),
        (2, "fountain"),
        (3, "furniture"),
        (4, "Home equipment"),
        (5, "natural")
    ]

    picture = models.ImageField(null=False, blank=False)
    introduction = models.TextField(null=True, blank=True)
    category = models.PositiveSmallIntegerField(null=False, blank=False, choices=CATEGORY, default=1)

    def __str__(self):
        return f"{self.id} {self.introduction}"


class TaskEvent(models.Model):
    participant = models.ForeignKey("Participant", null=False, blank=False, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)


class TaskEventImageReactionTime(models.Model):
    task_event = models.ForeignKey("TaskEvent", null=False, blank=False, on_delete=models.CASCADE)
    image = models.ForeignKey("Image", null=True, blank=True, on_delete=models.SET_NULL)
    reaction_time = models.PositiveIntegerField(null=True, blank=False, validators=[
        MaxValueValidator(3000),
    ])
