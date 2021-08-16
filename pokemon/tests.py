from django.test import TestCase
from django.urls import reverse

class PokemonAddViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/tame/1/')
        self.assertEqual(resp.status_code, 302)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('tame'))
        self.assertEqual(resp.status_code, 302)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('tame'))
        self.assertEqual(resp.status_code, 302)

        self.assertTemplateUsed(resp, 'main.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('tame'))
        self.assertEqual(resp.status_code, 302)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['author_list']) == 15)
