from rest_framework.viewsets import ModelViewSet

from api.serializers.course import SubjectSerializer
from course.models import Subject
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


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
    model = Subject


    def get_queryset(self):
        search = self.request.query_params.get("search")
        query = Q()
        if search:
            query &= Q(Q(name__icontains=search)
                       | Q(code__icontains=search)
                       )
        return self.model.objects.filter(query)