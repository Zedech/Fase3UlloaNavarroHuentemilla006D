from django.test import TestCase
from django.urls import reverse


from catalogo.models import Marca

class MarcaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Create 10 authors for pagination tests
        number_of_marca = 10
        for marca_id in range(number_of_marca):
            Marca.objects.create(
                marca=f' adidas{marca_id}',
            )

    
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('listamarca'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('listamarca'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'catalogo/marca_list.html')