from django.shortcuts import render

from card_inventory.models import Cards

def sets_index(request):
    # Get all unique set names
    sets = Cards.objects.order_by().values('set_name').distinct()

    # Transform each set name into a link and save as a dictionary item
    for s in sets:
        s['set_link'] = s['set_name'].replace(' ', '_')

    return render(request, 'sets_index.html', {'sets': sets})

def card_details_by_set(request, set_name):
    set_name_clean = set_name.replace('_', ' ')
    cards = Cards.objects.filter(set_name=set_name_clean)

    return render(request, 'card_details.html',
        {'cards': cards,
         'set_name': set_name_clean})
