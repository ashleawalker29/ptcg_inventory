from django.urls import path

from . import views

urlpatterns = [
    path('<str:set_name>/', views.card_details_by_set, name='card_details')
]
