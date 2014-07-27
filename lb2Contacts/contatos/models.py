import datetime
from django.db import models

# Create your models here.
from mongoengine import Document, StringField, EmailField, ReferenceField, connect, EmbeddedDocument, DateTimeField, \
    ListField, EmbeddedDocumentField
from mongoengine.django.auth import User
from lb2Contacts.settings import DBNAME

connect(DBNAME)

class Visita(EmbeddedDocument):
    data = DateTimeField(required=True,default=datetime.datetime.now())
    observacoes = StringField(required=True),
    tags = ListField(StringField(max_length=50))
    visitante = ReferenceField(User)

class Contato(Document):
    nome = StringField(max_length=60, required=True)
    email = EmailField(max_length=60)
    telefone = StringField(max_length=20)
    skype = StringField(max_length=60, required=True)
    visitas = ListField(EmbeddedDocumentField(Visita))
