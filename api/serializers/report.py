from rest_framework import serializers
from api.serializers.course import SubjectSerializer
from api.serializers.student import StudentSerializer
from report.models import Mark, ReportCard, Term
from django.db.models import Avg

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ("id","title")


class ReportCardSerializer(serializers.ModelSerializer):
    '''
    Used in Report Card Viewset.
    '''
    class Meta:
        model = ReportCard
        fields = ("id","student","term","year")

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["student"] = StudentSerializer(instance.student).data
        repr["term"] = instance.term.title
        return repr



class StudentReportCardSerializer(serializers.ModelSerializer):
    '''
    Used in Student Report Card API (Yearly). (Student removed to reduce redundancy)
    '''
    marks = serializers.SerializerMethodField()

    class Meta:
        model = ReportCard
        fields = ("id","term","year","marks")

    def get_marks(self,obj):
        marks = ReportMarkListSerializer(obj.marks.all(),many=True).data
        return marks
    
    def to_representation(self, instance):
        repr =  super().to_representation(instance)
        repr["term"] = instance.term.title
        return repr
    

class ReportCardDetailSerializer(StudentReportCardSerializer):
    '''
    Used in ReportCard Viewset's Detail View. (Student Added)
    '''
    student = StudentSerializer()
    # average_score_calc = serializers.SerializerMethodField()

    class Meta:
        model = ReportCard
        fields = ("id",'student',"term","year","marks","average_score")

        # fields = ("id",'student',"term","year","marks","average_score","average_score_calc")  # remove it
    
    # get_average_score_calc was to test  (remove it)
    # def get_average_score_calc(self,obj):
    #     return obj.marks.aggregate(Avg("score"))["score__avg"]




class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ("id","report_card","subject","score")


class ReportMarkListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    class Meta:
        model = Mark
        fields = ("id","subject","score")


class MarkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ("score",)