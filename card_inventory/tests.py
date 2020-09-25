from django.apps import apps
from django.test import TestCase
import pokemontcgsdk

from card_inventory.apps import CardInventoryConfig

class CardInventoryTests(TestCase):

    def test_card_inventory_app(self):
        self.assertEqual(CardInventoryConfig.name, 'card_inventory')
        self.assertEqual(apps.get_app_config('card_inventory').name, 'card_inventory')

    def test_sets_index(self):
        response = self.client.get('index/')

        self.assertEqual(response.status_code, 200)

    def test_cards_by_set_views(self):
        set_names = [Set.name for Set in pokemontcgsdk.Set.all()]

        for set_name in set_names:
            set_name_link = set_name.replace(' ', '_')
            response = self.client.get('index/%s/' % set_name_link)

            self.assertEqual(response.status_code, 200)

    def test_duplicate_cards_view(self):
        response = self.client.get('duplicate_cards/')

        self.assertEqual(response.status_code, 200)
