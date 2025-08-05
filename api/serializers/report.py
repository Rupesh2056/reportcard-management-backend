from rest_framework import serializers
from api.serializers.course import SubjectSerializer
from report.models import Mark, ReportCard, Term

class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = ("id","title")


class ReportCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportCard
        fields = ("id","student","term","year")


class ReportCardDetailSerializer(serializers.ModelSerializer):
    marks = serializers.SerializerMethodField()
    class Meta:
        model = ReportCard
        fields = ("id","student","term","year","marks")

    def get_marks(self,obj):
        marks = ReportMarkListSerializer(obj.marks.all(),many=True).data
        return marks


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ("id","report_card","subject","score")


class ReportMarkListSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    class Meta:
        model = Mark
        fields = ("id","subject","score")