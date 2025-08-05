from django.contrib import admin

from report.models import Mark, ReportCard, Term

# Register your models here.
admin.site.register([
    Term,
    ReportCard,
    Mark
    ])

