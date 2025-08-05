from django.db import models

from root.models import TimeStampModel

# Create your models here.

class Subject(TimeStampModel):
    name = models.CharField(max_length=125)
    code = models.CharField(unique=True)



    








