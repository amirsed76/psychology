from . import models
from django.contrib import admin


class ParticipantAdmin(admin.ModelAdmin):
    class HealthAdmin(admin.StackedInline):
        model = models.Health
        extra = 1

    class ParticipantAnswerAdmin(admin.StackedInline):
        model = models.ParticipantQuestionAnswer
        extra = 1

    model = models.Participant
    inlines = [HealthAdmin, ParticipantAnswerAdmin]


class TaskEventAdmin(admin.ModelAdmin):  # TODO show date
    list_display = (
        'participant', "jalali_date", "score", "sanderland_score", "reaction_time", "event_count", "jalali_next_date")
    

    class TaskEventImageAdmin(admin.StackedInline):
        model = models.TaskEventImageReactionTime
        extra = 1

    model = models.TaskEvent
    inlines = [TaskEventImageAdmin]


admin.site.register(models.Participant, ParticipantAdmin)
admin.site.register(models.Question)
admin.site.register(models.Image)
admin.site.register(models.TaskEvent, TaskEventAdmin)
