from django.apps import apps
from django.test import TestCase

from card_inventory.apps import CardInventoryConfig

class CardInventoryTests(TestCase):

    def test_card_inventory_app(self):
        self.assertEqual(CardInventoryConfig.name, 'card_inventory')
        self.assertEqual(apps.get_app_config('card_inventory').name, 'card_inventory')

    def test_cards_by_set_view(self):
        response = self.client.get('')

        self.assertEqual(response.status_code, 200)
