# calculations/urls.py

from django.urls import path
from . import views
# from .views import calculations
from django.contrib import admin
from django.urls import path, include
from obligor_data.views import home
from calculations import views as calculations_views  # Import your view
from calculations.admin import admin_site

urlpatterns = [
    path("run-ifrs17-model/", views.run_ifrs17_model, name="run_ifrs17_model"),
    path("run_model/", views.run_model, name="run_model"),
    path("model_run_status/<int:pk>/", views.model_run_status, name="model_run_status"),
    path(
        "fcf_vars/", views.fcf_vars_page, name="fcf_vars_page"
    ),  # For rendering the HTML
    path(
        "fcf_vars/api", views.fcf_vars_api, name="fcf_vars_api"
    ),  # For CRUD operations     # This should be defined
path("run-ifrs17-model/", calculations_views.run_ifrs17_model, name="run_ifrs17_model"),
    path("run_model/", calculations_views.run_model, name="run_model"),
    path("calculations/", calculations_views.run_model, name="calculations"),  # This will fix your error
    path("model_run_status/<int:pk>/", calculations_views.model_run_status, name="model_run_status"),
    path("fcf_vars/", calculations_views.fcf_vars_page, name="fcf_vars_page"),
    path("fcf_vars/api", calculations_views.fcf_vars_api, name="fcf_vars_api"),
]
