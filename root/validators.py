from django.core.exceptions import ValidationError
import datetime

def validate_score(value):
    if value > 100:
        raise ValidationError(f'{value} Cant be greater than 100')
    
def validate_year(value):
    this_year = datetime.date.today().year
    if value in range(this_year-4 , this_year +2):
        raise ValidationError(f'Please Enter Valid year. Valid range: {this_year-4} - {this_year +1}')