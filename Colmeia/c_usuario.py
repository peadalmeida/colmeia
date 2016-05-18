# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from app import models
from app.models import Usuario
from app.models import Endereco
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpRequest
from datetime import datetime
from Colmeia import p_perfil
from Colmeia import p_endereco
from django.db import connection
from app.forms import UsuarioForm
from app.forms import EnderecoForm

def incluir(request):
    objEndereco = Endereco.create(request.POST['CEP'],request.POST['Estado'],request.POST['Cidade'], request.POST['Bairro'],request.POST['Logradouro'],request.POST['Numero'],request.POST['Complemento'] )
    objEndereco.save()
    objEndereco = p_endereco.recuperaUltimoEndereco()
    objPerfil = p_perfil.recuperaPerfil('3')
    objUsuario = Usuario.create(objEndereco, objPerfil, request.POST['IndicadorTipoPessoa'],request.POST['CpfCnpj'],request.POST['Nome'],request.POST['Telefone1'],request.POST['Telefone2'],request.POST['Email'],request.POST['Senha'])
    objUsuario.save()
    form = UsuarioForm()
    end = EnderecoForm()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/site/indexSite.html',{'form': form, 'endereco': end},
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Início',
            'year':datetime.now().year,
        })
    )

#recupera todos os objetos
def recuperaUsuario():
    objUsuario = models.Usuario.objects.all()
    return objUsuario

#recupera todos um objeto especifico pelo id
def recuperaEncontro(idObj):
	objEncontro = models.Encontro.objects.get(id=idObj)
	return objEncontro