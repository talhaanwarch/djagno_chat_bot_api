from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.call_model.as_view())
    ]