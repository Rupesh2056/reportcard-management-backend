from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views.student import StudentModelViewSet

router = DefaultRouter()

router.register(r"student", StudentModelViewSet, basename="student_viewset")

urlpatterns = []
urlpatterns +=router.urls 





