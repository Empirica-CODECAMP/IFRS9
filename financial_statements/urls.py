from django.urls import path
from . import views

urlpatterns = [
    path('', views.financial_statements_landing, name='financial_statements_landing'),
]
