import decimal
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from root.celery import sync_report_average_score_task

from report.models import Mark

@receiver(post_save, sender=Mark)
def sync_average_score(sender, instance, created, **kwargs):
    sync_report_average_score_task.delay([instance.report_card.id]) # task in background to sync average
    
    