from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery import shared_task

from django.db.models import Avg
import decimal


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")

app = Celery("root")


app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")



@shared_task
def sync_report_average_score_task(report_card_ids):
    '''
     Takes in report_card_ids (iterable) and syncs the average_score for all reports.
    '''
    print("task called.....")
    from report.models import Mark, ReportCard

    for report_card_id in report_card_ids:
        report_card = ReportCard.objects.get(id=report_card_id)

        average_score = Mark.objects.filter(report_card=report_card).aggregate(average_score=Avg("score"))["average_score"]

        print(f"average score..............>>>>> {average_score}")
        average_score = decimal.Decimal(round(average_score,2))
        if report_card.average_score != average_score:
            print("not equal")
            report_card.average_score = average_score
            report_card.save()




