from rest_framework import serializers
from course.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    '''
    Used in Viewset and Report
    '''
    class Meta:
        model = Subject
        fields = ("id","name","code")