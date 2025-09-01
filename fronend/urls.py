from django.urls import path   # <-- BU SHART
from . import views



urlpatterns = [
    path('home/', views.index, name='index'),
    path('bars/', views.bars, name='bars'),
]
