from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.sets_index, name='sets_index'),
    path('index/<str:set_name>/', views.cards_by_set, name='card_details'),
    path('duplicate_cards/', views.duplicate_cards, name='duplicate_cards')
]
