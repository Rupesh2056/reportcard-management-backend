from rest_framework.viewsets import ModelViewSet

from api.serializers.report import MarkSerializer, ReportCardDetailSerializer, ReportCardSerializer, TermSerializer
from report.models import Mark, ReportCard, Term
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg,Prefetch
from rest_framework.permissions import IsAuthenticated

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
    pagination_class = None



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
    pagination_class = None

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ["list","retrieve"]:
            return ReportCardDetailSerializer
        return self.serializer_class




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
    permission_classes = [IsAuthenticated]
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
            
            report_cards = ReportCard.objects.filter(
                            student_id=student_id,year=year
                            ).prefetch_related(
                                Prefetch('marks', queryset=Mark.objects.select_related('subject'))
                                )
            marks = Mark.objects.filter(                 
                                    report_card__student_id=student_id,
                                    report_card__year=year
                                    ).values(
                                        "subject__name").annotate(
                                            avergae_score = Avg("score")
                                        )

            overall_average_score = ReportCard.objects.filter(
                            student_id=student_id,year=year
                            ).aggregate(
                                                        overall_score=Avg("marks__score")
                                                        )["overall_score"]
            

            data["reports"] = ReportCardDetailSerializer(report_cards,many=True).data
            data["overall_average_score"] = overall_average_score
            data["average_per_subject"] = list(marks)
            return Response(data=data)
        return Response(data={"message":"Please Provide Year and student_id"},status=400)