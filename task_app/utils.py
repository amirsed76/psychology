from . import models, constances
import datetime


def can_do_task(participant):
    if models.TaskEvent.objects.filter(participant=participant).count() == 1:
        last_event = models.TaskEvent.objects.get(participant=participant)
        if (datetime.datetime.now().date() - last_event.date_time.date()).days < constances.TASK_DAY_DURATION:
            return False

    return True


def get_task_date(participant):
    if models.TaskEvent.objects.filter(participant=participant).count() == 1:
        last_event = models.TaskEvent.objects.get(participant=participant)
        if (datetime.datetime.now().date() - last_event.date_time.date()).days < constances.TASK_DAY_DURATION:
            return last_event.date_time.date() + datetime.timedelta(days=constances.TASK_DAY_DURATION)

    return None


def convert_digit(input_text):
    intab = '۱۲۳۴۵۶۷۸۹۰١٢٣٤٥٦٧٨٩٠'
    outtab = '12345678901234567890'
    translation_table = str.maketrans(intab, outtab)
    output_text = input_text.translate(translation_table)
    return output_text


