from django.db import models

from root.models import TimeStampModel

# Create your models here.

class Student(TimeStampModel):
    name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True,null=True)
