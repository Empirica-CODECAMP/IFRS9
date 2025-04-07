from django.urls import path
from . import views

urlpatterns = [
    path('', views.ecl_landing, name='ecl_landing'),
    path('ecl-reports/', views.ecl_report_list, name='ecl_report_list'),
    path('stage-allocations/', views.stage_allocation_list, name='stage_allocation_report_list'),
    path('loss-allowances/', views.loss_allowance_list, name='loss_allowance_list'),
    path('credit-risk-exposures/', views.credit_risk_exposure_list, name='credit_risk_exposure_list'),
]
