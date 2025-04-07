from django.urls import include, path

from analyis import views
from .views import *

urlpatterns = [
    path("", obligor_list, name="obligor_list"),
    path('', home, name='home'),
    # path('loan-data/', views.loan_data_list('request'), name='loan_data_list'),

    # path("predict/", predict_ecl, name="predict_ecl"),
      # Include ECL Calculations URLs here
  
]
