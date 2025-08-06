from rest_framework.viewsets import ModelViewSet

from api.serializers.report import MarkSerializer, ReportCardDetailSerializer, ReportCardSerializer, StudentReportCardSerializer, TermSerializer
from api.serializers.student import StudentSerializer
from report.models import Mark, ReportCard, Term
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg,Prefetch
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q,Func,FloatField,Value

from student.models import Student

class TermModelViewSet(ModelViewSet):
    '''
    CRUD for Term
    '''
    permission_classes = [IsAuthenticated]
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
    ]
    serializer_class = TermSerializer
    queryset = Term.objects.all()
    model = Term

    def get_queryset(self):
        search = self.request.query_params.get("search")
        query = Q()
        if search:
            query &= Q(title__icontains=search)
        return self.model.objects.filter(query)



class ReportCardViewSet(ModelViewSet):
    '''
    CRU  for ReportCard
    '''
    permission_classes = [IsAuthenticated]
    http_method_names = [
        "get",
        "post",
    ]
    serializer_class = ReportCardSerializer
    queryset = ReportCard.objects.all()
    model = ReportCard

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ["retrieve"]:
            return ReportCardDetailSerializer
        return self.serializer_class
    
    def get_queryset(self):
        term = self.request.query_params.get("term")
        year = self.request.query_params.get("year")
        search = self.request.query_params.get("search")

        query = Q()

        try:
            if term:
                query &= Q(term_id = int(term))

            if year:
                query &= Q(year=int(year))
        except:
            pass
        if search:
            query &= Q(Q(student__name__icontains=search)
                       | Q(student__email__icontains=search)
                       )


        return self.model.objects.filter(query)




class MarkViewSet(ModelViewSet):
    '''
    CRU  for Mark
    '''
    permission_classes = [IsAuthenticated]
    http_method_names = [
        "post",
        "patch",
        "put"
    ]
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()



class StudentReportCardAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        data = {}
        student_id = self.request.query_params.get("student_id")
        year = self.request.query_params.get("year")
        
        if student_id and year:
            try:
                student_id = int(student_id)
                year = int(year)
            except:
                return Response(data={"message":"Invalid format of year or student_id"})
            
            query = Q(year=year,student_id=student_id)


            # for report list along with subject marks
            report_cards = ReportCard.objects.filter(
                           query
                            ).select_related("term").prefetch_related(
                                Prefetch('marks', queryset=Mark.objects.select_related('subject'))
                                )
            
            # for aggregation (average score per subject)
            subject_wise_average = Mark.objects.filter(                 
                                    report_card__student_id=student_id,
                                    report_card__year=year
                                    ).values(
                                        "subject__name").annotate(average_score=Func(
                                                            Avg("score"),
                                                            Value(2),
                                                            function='ROUND',
                                                            output_field=FloatField()
                                                        ))

            overall_average_score = ReportCard.objects.filter(
                                                            query
                                                             ).aggregate(
                                                            overall_score=Avg("marks__score")
                                                            )["overall_score"]


            
            data["student"] = StudentSerializer(Student.objects.get(id=student_id)).data
            data["reports"] = StudentReportCardSerializer(report_cards,many=True).data
            data["average_per_subject"] = list(subject_wise_average)
            data["overall_average_score"] = round(overall_average_score,2)
            return Response(data=data)
        return Response(data={"message":"Please Provide Year and student_id"},status=400)