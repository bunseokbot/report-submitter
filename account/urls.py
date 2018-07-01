from django.urls import path

from . import views
from .views import LoginView, JoinView


urlpatterns = [
    path('login/', LoginView.as_view(), name='account_login'),
    path('logout/', views.logout, name='account_logout'),
    path('join/', JoinView.as_view(), name='account_join'),
]
