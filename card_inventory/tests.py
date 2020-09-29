from django.apps import apps
from django.test import TestCase
import pokemontcgsdk

from card_inventory.apps import CardInventoryConfig
from card_inventory.models import Sets

class CardInventoryTests(TestCase):

    def setUp(self):
        """ Populate the `Sets` DB with all necessary information. """
        released_sets = pokemontcgsdk.Set.all()
        for set_info in released_sets:
            Sets.objects.create(set_name=set_info.name, set_code=set_info.code,
                                max_cards=set_info.total_cards)

    def test_card_inventory_app(self):
        self.assertEqual(CardInventoryConfig.name, 'card_inventory')
        self.assertEqual(apps.get_app_config('card_inventory').name, 'card_inventory')

    def test_sets_index(self):
        response = self.client.get('/index/')

        self.assertEqual(response.status_code, 200)

    def test_cards_by_set_views(self):
        set_names = [Set.name for Set in pokemontcgsdk.Set.all()]

        for set_name in set_names:
            set_name_link = set_name.replace(' ', '_')
            response = self.client.get('/index/%s/' % set_name_link)

            self.assertEqual(response.status_code, 200)

    def test_duplicate_cards_view(self):
        response = self.client.get('/duplicate_cards/')

        self.assertEqual(response.status_code, 200)
