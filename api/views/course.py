from rest_framework.viewsets import ModelViewSet

from api.serializers.course import SubjectSerializer
from course.models import Subject
from rest_framework.permissions import IsAuthenticated

class SubjectModelViewSet(ModelViewSet):
    '''
    CRUD for Student
    '''
    permission_classes = [IsAuthenticated]
    http_method_names = [
        "get",
        "post",
        "delete",
        "put",
        "patch",
    ]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    pagination_class = None