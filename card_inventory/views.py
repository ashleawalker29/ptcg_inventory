from django.shortcuts import render

from card_inventory.models import Cards

def card_details_by_set(request, set_name):
    set_name_clean = set_name.replace('_', ' ').title()
    cards = Cards.objects.filter(set_name=set_name_clean)

    return render(request, 'card_details.html',
        {'cards': cards,
         'set_name': set_name_clean})
