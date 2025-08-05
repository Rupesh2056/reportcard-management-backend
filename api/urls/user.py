from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = (
    path("user/login/", TokenObtainPairView.as_view(), name="login"),

)


