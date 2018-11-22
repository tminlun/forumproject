from django.urls import path
from .views import LoginView


urlpatterns = [
    path('login_or_registered/', LoginView.as_view(), name="login_or_registered"),
]