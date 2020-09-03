from django.shortcuts import render
import pokemontcgsdk

from card_inventory.models import Cards

def sets_index(request):
    sets = [{'name': Set.name, 'link': Set.name.replace(' ', '_'),
             'series': Set.series, 'release_date': Set.release_date,
             'logo_url': Set.logo_url, 'symbol_url': Set.symbol_url}
            for Set in pokemontcgsdk.Set.all()]

    return render(request, 'sets_index.html', {'sets': sets})

def cards_by_set(request, set_name):
    set_name_clean = set_name.replace('_', ' ')
    cards = Cards.objects.filter(set_name=set_name_clean)

    return render(request, 'cards_by_set.html',
        {'cards': cards,
         'set_name': set_name_clean})
