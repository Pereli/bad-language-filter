from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filterapp/', views.censor, name='censor')
]