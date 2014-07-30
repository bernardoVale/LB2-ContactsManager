# coding=utf-8
from mongoforms import MongoForm
from lb2Contacts.contatos.models import Contato

__author__ = 'bernardovale'

class ContatoForm(MongoForm):
    """
    Classe utilizada para testar o formulário de
    inserção de novos contatos.
    """
    class Meta:
        document = Contato
        fields = ('email','empresa','nome','telefone','celular','endereco','skype')