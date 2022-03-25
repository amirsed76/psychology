from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

from django.core.validators import MaxValueValidator, MinValueValidator
import jdatetime


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
    ], default=1320)
    education_level = models.PositiveSmallIntegerField(null=False, blank=False, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    mobile_number = models.CharField(max_length=11, validators=[
        RegexValidator('^09[0-9]{9}$', message='شماره ی موبایل معتبر نمیباشد.')], null=False, blank=False, unique=True)
    gender = models.CharField(max_length=6, choices=Gender, null=False, blank=False)

    def __str__(self):
        return f"{self.name} {self.family_name} {self.mobile_number}"

    def event_count(self):
        return len(list(TaskEvent.objects.filter(participant=self)))


class Health(models.Model):
    participant = models.OneToOneField("Participant", null=False, blank=False, on_delete=models.CASCADE)
    get_covid_19 = models.PositiveSmallIntegerField(null=False, blank=False, validators=[
        MaxValueValidator(2),
        MinValueValidator(0)
    ])
    get_drug = models.BooleanField(null=False, blank=False)
    mental_disorder = models.TextField(null=False, blank=True)
    get_medicine = models.BooleanField(null=False, blank=False, default=False)

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
        ("towner", "towner"),
        ("fountain", "fountain"),
        ("furniture", "furniture"),
        ("kettle", "kettle"),
        ("landscap", "landscap"),
        ("spoon", "spoon"),
        ("tools", "tools"),
        ("tree", "tree"),
        ("flower", "flower"),
        ("test", "test")

    ]

    picture = models.ImageField(null=False, blank=False)
    introduction = models.TextField(null=True, blank=True)
    category = models.CharField(null=False, blank=False, choices=CATEGORY, default="towner", max_length=10)

    def __str__(self):
        return f"{self.id} {self.category}  {self.picture}"


class TaskEvent(models.Model):
    participant = models.ForeignKey("Participant", null=False, blank=False, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def get_score(self):
        seen = []
        wrongs = 0
        randomly = 0

        for image_time in self.taskeventimagereactiontime_set.all():

            if image_time.reaction_time is not None and image_time.reaction_time < 300:
                randomly += 1

            elif image_time.image.id not in seen and image_time.reaction_time is not None:
                wrongs += 1

            elif image_time.image.id in seen and image_time.reaction_time is None:
                wrongs += 1

            seen.append(image_time.image.id)

        if randomly == 50:
            return 0  # TODO raise Exception

        return int(((50 - (wrongs + randomly)) / (50 - randomly)) * 100)

    def __str__(self):
        date = jdatetime.datetime.fromgregorian(datetime=self.date_time).date()
        return f"{self.participant.name} {self.participant.family_name}*** {self.participant.mobile_number} *** {self.participant.event_count()} *** {date.year}_{date.month}_{date.day} *** {self.get_score()}"


class TaskEventImageReactionTime(models.Model):
    task_event = models.ForeignKey("TaskEvent", null=False, blank=False, on_delete=models.CASCADE)
    image = models.ForeignKey("Image", null=True, blank=True, on_delete=models.SET_NULL)
    reaction_time = models.PositiveIntegerField(null=True, blank=False, validators=[
        MaxValueValidator(3000),
    ])
