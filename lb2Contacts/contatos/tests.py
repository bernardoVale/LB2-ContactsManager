# coding=utf-8
from django.utils.unittest.case import TestCase
from mongoengine.django.auth import User
from lb2Contacts.contatos.models import Contato, Visita, UserPrefs


class ContatoTestCase(TestCase):
    def setUp(self):
        Contato.drop_collection()
        self.contatoOK = Contato(
            nome = 'Joao',
            telefone = '4399651538',
            skype = 'joaoskype',
        ).save()
        User.drop_collection()
        self.u = User.create_user('wilmutt','vilmo','wilmutt@gmail.com')

    def test_total_objects(self):
        """
        Faz um teste de contagem de objetos
        :return:
        """
        total = Contato.objects.count()
        self.assertEqual(1,total)

    def test_contato_existente(self):
        """
        Verifica se o contato inserido no setup foi persistido
        :return:
        """
        self.assertEqual(self.contatoOK.nome,'Joao')

    def test_createUser(self):
        """
        Testa a propriedade de criação de usuários
        :return:
        """
        self.assertEqual(self.u.username,'wilmutt')

    def test_novaVisita(self):
        """
        Adiciona uma visita ao Contato e verifica a persistencia.
        :return:
        """
        visita = Visita (
            observacoes = 'O nene caiu no estradon.',
            tags = ['NENE','BIXO BURRU'],
            visitante = self.u
        )
        self.contatoOK.update(add_to_set__visitas=visita)
        c_before = self.contatoOK.save()
        c = Contato.objects.get_or_create(nome='Joao')

        self.assertNotEqual(c_before,c)
        self.assertEqual(len(c[0].visitas[0].tags),2)
        self.assertEqual(c[0].visitas[0].visitante.username,'wilmutt')
        self.assertEqual(c[0].visitas[0].observacoes,'O nene caiu no estradon.')

    def test_user_prefs(self):
        """
        Verifica se é possível adicionar as preferencias do usuário ao contato
        :return:
        """
        user_prefs = UserPrefs(
            user = self.u,
            alerta = 'SEMANAL'
        )
        self.contatoOK.update(add_to_set__user_prefs=user_prefs)
        self.contatoOK.save()
        cc = Contato.objects.get(nome='Joao')
        self.assertEqual(cc.user_prefs[0].user.username,'wilmutt')
        self.assertEqual(cc.user_prefs[0].alerta,'SEMANAL')

    def test_update_user_prefs(self):
        """
        Testa a atualização do alerta de um usuário de semanal para mensal
        para um determinado contato.
        :return:
        """
        user_prefs = UserPrefs(
            user = self.u,
            alerta = 'SEMANAL'
        )
        self.contatoOK.update(add_to_set__user_prefs=user_prefs)
        self.contatoOK.save()
        user_prefs.alerta = 'MENSAL'
        Contato.objects(id=self.contatoOK.pk).update(set__user_prefs=user_prefs)