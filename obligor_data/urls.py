from django.urls import include, path

from analyis import views
from .views import *
from .views import (
    neural_networks_view,
    factor_models_view,
    stage1_view,
    stage2_view,
    stage3_view
)


urlpatterns = [
    path("", obligor_list, name="obligor_list"),
    # path('', home, name='home'),
        path('', views.landing, name='landing'),            # 👈 now the default landing page
        path('dashboard/', views.home, name='ifrs9_home'),
    # path('loan-data/', views.loan_data_list('request'), name='loan_data_list'),

    # path("predict/", predict_ecl, name="predict_ecl"),
      # Include ECL calculations URLs here
    path("ecl/", include("ecl_calculations.urls")),
    path('neural_networks/', neural_networks_view, name='neural_networks'),
    path('factor_models/', factor_models_view, name='factor_models'),
    path('stage1/', stage1_view, name='stage1'),
    path('stage2/', stage2_view, name='stage2'),
    path('stage3/', stage3_view, name='stage3'),
    path('landing/', landing, name='landing_home'),


    
]
