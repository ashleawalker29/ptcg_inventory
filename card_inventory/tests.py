from django.test import TestCase
from django.urls import reverse

class CardInventoryTests(TestCase):

    def test_cards_by_set_view(self):
        response = self.client.get('')

        self.assertEqual(response.status_code, 200)
