from django.urls import path
from . import views

urlpatterns = [
    path('', views.financial_statements_landing, name='financial_statements_landing'),
     path('', views.financial_statements_landing, name='financial_statements_landing'),
    path('view/<str:statement_type>/<int:file_id>/', views.view_excel, name='view_excel'),
]
