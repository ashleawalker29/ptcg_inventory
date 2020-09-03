from django.shortcuts import render
import pokemontcgsdk

from card_inventory.models import Cards

def sets_index(request):
    sets = [{'name': Set.name, 'link': Set.name.replace(' ', '_'),
             'series': Set.series, 'release_date': Set.release_date,
             'logo_url': Set.logo_url, 'symbol_url': Set.symbol_url}
            for Set in pokemontcgsdk.Set.all()]

    for s in sets:
        try:
            quantity_normal = sum([card.quantity_normal for card in Cards.objects.filter(set_name=s['name'])])
            quantity_reverse = sum([card.quantity_reverse for card in Cards.objects.filter(set_name=s['name'])])
            quantity_holo = sum([card.quantity_holo for card in Cards.objects.filter(set_name=s['name'])])
        except:
            quantity_normal, quantity_reverse, quantity_holo = None, None, None

        s['quantity_normal'] = quantity_normal
        s['quantity_reverse'] = quantity_reverse
        s['quantity_holo'] = quantity_holo

    return render(request, 'sets_index.html', {'sets': sets})

def cards_by_set(request, set_name):
    set_name_clean = set_name.replace('_', ' ')
    cards = Cards.objects.filter(set_name=set_name_clean)

    return render(request, 'cards_by_set.html',
        {'cards': cards,
         'set_name': set_name_clean})
