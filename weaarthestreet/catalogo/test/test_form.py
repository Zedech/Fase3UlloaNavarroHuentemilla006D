from django.test import TestCase
from catalogo.forms import MarcaForm
from catalogo.models import Marca


class MarcaFormsTest(TestCase):
    def test_valid_form(self):
        gg= Marca.objects.create(marca='Nike, Zapatilla')
        data = {'listamarca': Marca,}
        form = MarcaForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form(self):
        gg= Marca.objects.create(marca='')
        data = {'listamarca': Marca,}
        form = MarcaForm(data=data)
        self.assertFalse(form.is_valid())