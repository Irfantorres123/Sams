from django.urls import path
from . import views

from user.views import LoginView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path("logout/", views.logout_request, name="logout"),
    path('home', views.homepage, name='home')
]
