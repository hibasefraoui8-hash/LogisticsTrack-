from django.urls import path
from . import views

urlpatterns = [
    path('', views.rechercher, name='dashboard_client'),
    path('detail/<int:colis_id>/', views.detail_colis, name='detail_colis'),
]