from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views.course import SubjectModelViewSet

router = DefaultRouter()

router.register(r"subject", SubjectModelViewSet, basename="subject_viewset")

urlpatterns = router.urls 





