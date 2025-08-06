from django.core.management.base import BaseCommand

from student.models import Student
from course.models import Subject
from report.models import Term,ReportCard,Mark
import random
import decimal


def create_students():
    students = []
    last_student = Student.objects.last()

    last_student_id = last_student.id if last_student else 0
      
    for i in range(1000):
        student_dict = dict(name=f"Student {last_student_id+1}",email=f"stud{last_student_id+1}@mail.com")
        last_student_id += 1
        students.append(Student(**student_dict))
    
    return Student.objects.bulk_create(students)
    print(f"{i+1} Students created.")


def create_terms():
    terms = ["First","Second","Third","Final"]
    for term_title in terms:
            Term.objects.get_or_create(title=f"{term_title} Term")


def create_subjects():
    subjects = []
    last_subject_id = Subject.objects.last().id if Subject.objects.last() else 0
    for i in range(5):
        subjects.append(Subject(name=f"Subject {last_subject_id+1}",code=f"CS-{last_subject_id+1}"))
        last_subject_id += 1
    return Subject.objects.bulk_create(subjects)



def create_report_cards(students):
    terms = Term.objects.all()
    years = [2025,2026]
    report_cards=[]
    for student in students:
        for term in terms:
            for year in years:    
                report_cards.append(ReportCard(student=student,term=term,year=year))
    return ReportCard.objects.bulk_create(report_cards)


def create_marks(students,subjects,reports):
    marks = []
    for report in reports:
        for subject in subjects:
            random_score = decimal.Decimal(random.randint(0,100))
            marks.append(Mark(report_card=report,subject=subject,score=random_score))
    Mark.objects.bulk_create(marks)
    
     


class Command(BaseCommand):
    """
    Assigns full_title to categories
    python manage.py sync_category_full_title
    """
    help = "Assigns full_title to Categories"

    def handle(self, **options):

        students = create_students()
        create_terms()
        subjects = create_subjects()
        reports = create_report_cards(students)
        create_marks(students,subjects,reports)






        


        


        
