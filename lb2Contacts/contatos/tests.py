# coding=utf-8
from django.utils.unittest.case import TestCase
from lb2Contacts.contatos.models import Contato


class ContatoTestCase(TestCase):
    def setUp(self):
        Contato.drop_collection()
        self.contatoOK = Contato(
            nome = 'Joao',
            telefone = '4399651538',
            skype = 'joaoskype',
        ).save()

    def test_total_objects(self):
        total = Contato.objects.count()
        self.assertEqual(1,total)

    def test_contato_existente(self):
        self.assertEqual(self.contatoOK.nome,'Joao')
