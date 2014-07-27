# coding=utf-8
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from mongoengine.django import auth
from mongoengine.django.auth import User

@login_required
def home(request):
    return render_to_response('home.html',
                              context_instance=RequestContext(request))


def login(request):
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
    auth_logout(request)
    return render_to_response('login.html',
                          context_instance=RequestContext(request))