from rest_framework.viewsets import ModelViewSet

from api.serializers.student import StudentSerializer
from student.models import Student
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


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
    permission_classes = [IsAuthenticated]
 


    def get_queryset(self):
        search = self.request.query_params.get("search")
        query = Q()
        if search:
            query &= Q(Q(name__icontains=search)
                       | Q(email__icontains=search)
                       )
        return Student.objects.filter(query)