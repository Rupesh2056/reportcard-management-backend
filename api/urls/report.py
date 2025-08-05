from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views.report import MarkViewSet, ReportCardViewSet, StudentReportCardAPIView, TermModelViewSet

router = DefaultRouter()

router.register(r"terms", TermModelViewSet, basename="term_viewset")
router.register(r"report-cards", ReportCardViewSet, basename="reportcard_viewset")
router.register(r"marks", MarkViewSet, basename="mark_viewset")

urlpatterns = [
    path("student-report-card/",StudentReportCardAPIView.as_view())
]

urlpatterns += router.urls 





