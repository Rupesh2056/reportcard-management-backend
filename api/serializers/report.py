from rest_framework import serializers
from api.serializers.course import SubjectSerializer
from api.serializers.student import StudentSerializer
from report.models import Mark, ReportCard, Term

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ("id","title")


class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = ("id","student","term","year")

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["student"] = StudentSerializer(instance.student).data
        repr["term"] = instance.term.title
        return repr



class StudentReportCardSerializer(serializers.ModelSerializer):
    marks = serializers.SerializerMethodField()
    # student = StudentSerializer()

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
    student = StudentSerializer()

    class Meta:
        model = ReportCard
        fields = ("id",'student',"term","year","marks")




class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ("id","report_card","subject","score")


class ReportMarkListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    class Meta:
        model = Mark
        fields = ("id","subject","score")