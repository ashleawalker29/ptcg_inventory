from django.urls import path

from . import views

urlpatterns = [
    path('', views.sets_index, name='sets_index'),
    path('<str:set_name>/', views.card_details_by_set, name='card_details')
]
