from django.db import models

from course.models import Subject
from root.models import TimeStampModel
from root.validators import validate_score,validate_year
from student.models import Student
import decimal

# Create your models here.
class Term(TimeStampModel):
    title = models.CharField(max_length=25)

class ReportCard(TimeStampModel):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="report_cards")
    term = models.ForeignKey(Term,on_delete=models.PROTECT,related_name="report_cards")
    year = models.PositiveIntegerField(validators=[validate_year])
    average_score =  models.DecimalField(max_digits=5,decimal_places=2,default=decimal.Decimal(0.0),
                                validators=[validate_score])

    class Meta:
        unique_together = ('student','term','year')        
        indexes = [
                    models.Index(fields=['student', 'year']),
                ]


class Mark(TimeStampModel):
    report_card = models.ForeignKey(ReportCard,on_delete=models.CASCADE,related_name="marks")
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,related_name="marks")
    score = models.DecimalField(max_digits=5,decimal_places=2,default=decimal.Decimal(0.0),
                                validators=[validate_score])

    class Meta:
        unique_together = ('report_card','subject')

