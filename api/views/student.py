from rest_framework.viewsets import ModelViewSet

from api.serializers.student import StudentSerializer
from student.models import Student

class StudentModelViewSet(ModelViewSet):
    '''
    CRUD for Student
    '''
    # permission_classes = [IsAuthenticated]
    http_method_names = [
        "get",
        "post",
        "delete",
        "put",
        "patch",
    ]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    pagination_class = None