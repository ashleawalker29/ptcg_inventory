from django.shortcuts import render
import pokemontcgsdk

from card_inventory.models import Cards

def sets_index(request):
    sets = [{'name': Set.name, 'link': Set.name.replace(' ', '_'),
             'series': Set.series, 'release_date': Set.release_date,
             'logo_url': Set.logo_url, 'symbol_url': Set.symbol_url}
            for Set in pokemontcgsdk.Set.all()]

    for s in sets:
        s['quantity_normal'] = sum(
            [card.quantity_normal or 0 for card in Cards.objects.filter(set_name=s['name'])])
        s['quantity_reverse'] = sum(
            [card.quantity_reverse or 0 for card in Cards.objects.filter(set_name=s['name'])])
        s['quantity_holo'] = sum(
            [card.quantity_holo or 0 for card in Cards.objects.filter(set_name=s['name'])])

    return render(request, 'sets_index.html', {'sets': sets})

def cards_by_set(request, set_name):
    set_name_clean = set_name.replace('_', ' ')
    cards = Cards.objects.filter(set_name=set_name_clean)

    return render(request, 'cards_by_set.html',
        {'cards': cards,
         'set_name': set_name_clean})

def duplicate_cards(request):
    cards = Cards.objects.all()
    cards = [card for card in cards
             if (card.quantity_normal + card.quantity_holo + card.quantity_reverse) > 4]

    return render(request, 'duplicate_cards.html', {'cards': cards})
