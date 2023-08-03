from django.urls import path
from . import views

urlpatterns = [
    path('', views.shulte_table, name='shulte_table'),
]
