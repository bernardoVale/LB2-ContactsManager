#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import *

urlpatterns = patterns('',
    url(r'^$', 'lb2Contacts.contatos.views.home'),
    url(r'^login/', 'lb2Contacts.contatos.views.login'),
    url(r'^logout/', 'lb2Contacts.contatos.views.logout'),
    url(r'^contato/', 'lb2Contacts.contatos.views.novocontato'),
)