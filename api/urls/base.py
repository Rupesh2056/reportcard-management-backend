from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path

from .user import urlpatterns as user_url_patterns
from .student import urlpatterns as student_url_patterns
from .course import urlpatterns as course_url_patterns
from .report import urlpatterns as report_url_patterns


schema_view = get_schema_view(
    openapi.Info(
        title="API Docs for Report Card",
        default_version="v1",
        description="API Swagger",
        contact=openapi.Contact(email="chaulagainrupesh@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = (
    [
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "docs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]
)
urlpatterns += student_url_patterns
urlpatterns += user_url_patterns
urlpatterns += course_url_patterns
urlpatterns += report_url_patterns

