# coding=utf-8
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from mongoengine import Q
from mongoengine.django import auth
from mongoengine.django.auth import User
from lb2Contacts.contatos.forms import ContatoForm
from lb2Contacts.contatos.models import Contato


@login_required
def home(request):
    """
    Método da tela inicial.
    :param request:
    :return:
    """
    if request.method == 'POST':
        #Lista de contatos
        contacts_list = Contato.objects\
            (Q(nome__icontains=request.POST['search'])
             | Q(empresa__icontains=request.POST['search']))
        return render_to_response('home.html',{'contacts_list':contacts_list},
                              context_instance=RequestContext(request))
    return render_to_response('home.html',
                              context_instance=RequestContext(request))


def login(request):
    """
    Método da tela de Login
    :param request:
    :return:
    """
    #User.create_user('bernardo.vale','contacts1992','bernardosilveiravale@gmail.com')
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return render_to_response('home.html',
                            context_instance=RequestContext(request))
            #TODO Adicionar erro de validação caso não autenticou
    else:
        #TODO Adicionar validação para usuário autenticado não entrar no /login
        return render_to_response('login.html',
                          context_instance=RequestContext(request))

def logout(request):
    """
    Método de logout. Ação do botão logout
    :param request:
    :return:
    """
    auth_logout(request)
    return render_to_response('login.html',
                          context_instance=RequestContext(request))

@login_required
def novocontato(request):
    """
    Método da tela de novo contato.
    :param request:
    :return:
    """

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            Contato().wrap(request.POST).save()
        else:
            return render_to_response('contato.html',{'form' : form},
                          context_instance=RequestContext(request))
    return render_to_response('contato.html',
                          context_instance=RequestContext(request))

@login_required
def visita(request):
    return render_to_response('visita.html',
                          context_instance=RequestContext(request))