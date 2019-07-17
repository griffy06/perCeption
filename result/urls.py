from django.urls import path
from . import views

urlpatterns = [
    path('positive/', views.positive, name='positive'),
    path('negative/', views.negative, name='negative'),
    path('neutral/', views.neutral, name='neutral'),

]