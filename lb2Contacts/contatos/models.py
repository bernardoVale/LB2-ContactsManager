# coding=utf-8
import datetime
from django.db import models

# Create your models here.
from mongoengine import Document, StringField, EmailField, ReferenceField, connect, EmbeddedDocument, DateTimeField, \
    ListField, EmbeddedDocumentField
from mongoengine.django.auth import User
from lb2Contacts.settings import DBNAME

connect(DBNAME)

class Visita(EmbeddedDocument):
    """
    Define um momento em que um determinado usuário
    interagiu ou visitou um contato da LB2.
    """

    data = DateTimeField(required=True,default=datetime.datetime.now())
    observacoes = StringField(required=True)
    tags = ListField(StringField(max_length=50))
    visitante = ReferenceField(User)

class UserPrefs(EmbeddedDocument):
    """
    Preferências do usuário para um determinado contato
    """

    ALERTAS = ("SEMANAL","QUINZENAL","MENSAL","SEM ALERTA")

    alerta = ListField(StringField(), choices=ALERTAS)
    user = ReferenceField(User)

class Contato(Document):
    """
    Documento pai que será gerido em todo o sistema.
    Define um contato (cliente da LB2) que um ou mais usuários
    poderam interagir.
    """

    nome = StringField(max_length=60, required=True)
    email = EmailField(max_length=60)
    telefone = StringField(max_length=20)
    celular = StringField(max_length=20)
    endereco = StringField(max_length=80)
    skype = StringField(max_length=60, required=True)
    visitas = ListField(EmbeddedDocumentField(Visita))
    user_prefs = ListField(EmbeddedDocumentField(UserPrefs))
