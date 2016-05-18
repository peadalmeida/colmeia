"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime


#PAGINA INICIAL DO SITE (GERAL)
def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/site/indexSite.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Início',
            'year':datetime.now().year,
        })
    )

#PAGINA INICIAL DO SISTEMA
def inicio(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Index',
            'year':datetime.now().year,
        })
    )


#PAGINA INICIAL DO SISTEMA
def search(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/geral/resultados.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Resultados',
            'year':datetime.now().year,
        })
    )


def s_quemSomos(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/site/s_quemSomos.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Quem Somos',
            'year':datetime.now().year,
        })
    )

def s_contato(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/site/s_contato.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Contato',
            'year':datetime.now().year,
        })
    )
def quemSomos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/geral/quemSomos.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Quem Somos',
            'year':datetime.now().year,
        })
    )

def admin(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/admin/admin.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Administrador',            
            'year':datetime.now().year,
        })
    )

def prestadores(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/admin/prestadores.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Prestadores',            
            'year':datetime.now().year,
        })
    )

def contratantes(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/admin/contratantes.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Contratantes',            
            'year':datetime.now().year,
        })
    )

def relatorioAdm(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/admin/relatorioAdm.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Relatorios',            
            'year':datetime.now().year,
        })
    )

#VIEWS PRESTADORES
def cadPrestador(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/prestador/frm_prestador.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Cad.Prestador',
            'year':datetime.now().year,
        })
    )

def servPrestados(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/prestador/servPrestados.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Serv.Prestados',
            'year':datetime.now().year,
        })
    )

def colmeiaPontos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/prestador/colmeiaPontos.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | ColPontos',
            'year':datetime.now().year,
        })
    )




#VIEWS CONTRATANTES
def cadContratante(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contratante/frm_contratante.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Cad. Contratante',
            'year':datetime.now().year,
        })
    )


def servContratados(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contratante/frm_contratante.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Serv.Contratados',
            'year':datetime.now().year,
        })
    )

def relContratante(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contratante/relatorioContratante.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Relatorios Contratante',
            'year':datetime.now().year,
        })
    )
def sair(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Inicio',
            'year':datetime.now().year,
        })
    )



def login(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/geral/login.html',
        context_instance = RequestContext(request,
        {
            'title':'Colmeia | Login',
            'year':datetime.now().year,
        })
    )
