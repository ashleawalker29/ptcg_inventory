from django.shortcuts import render
import pokemontcgsdk

from card_inventory.models import Cards, Sets

def sets_index(request):
    sets = [{'name': Set.name, 'code': Set.code , 'link': Set.name.replace(' ', '_'),
             'series': Set.series, 'release_date': Set.release_date,
             'logo_url': Set.logo_url, 'symbol_url': Set.symbol_url}
            for Set in pokemontcgsdk.Set.all()]

    for s in sets:
        s['quantity_normal'] = sum(
            [card.quantity_normal or 0 for card in Cards.objects.filter(set_code=s['code'])])
        s['quantity_reverse'] = sum(
            [card.quantity_reverse or 0 for card in Cards.objects.filter(set_code=s['code'])])
        s['quantity_holo'] = sum(
            [card.quantity_holo or 0 for card in Cards.objects.filter(set_code=s['code'])])

    return render(request, 'sets_index.html', {'sets': sets})

def cards_by_set(request, set_name):
    set_name_clean = set_name.replace('_', ' ')
    set_info = Sets.objects.get(set_name=set_name_clean)

    cards = Cards.objects.filter(set_code=set_info.set_code)

    return render(request, 'cards_by_set.html',
        {'set_info': set_info,
         'cards': cards})

def duplicate_cards(request):
    cards = Cards.objects.all()
    cards = [card for card in cards
             if (card.quantity_normal + card.quantity_holo + card.quantity_reverse) > 4]

    return render(request, 'duplicate_cards.html', {'cards': cards})
