"""
Definition of urls for Colmeia.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
import p_usuario
import c_usuario

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.index', name='index'),
    url(r'^inicio', 'app.views.inicio', name='inicio'),
    url(r'^search', 'app.views.search', name='search'),
    url(r'^quemSomos', 'app.views.quemSomos', name='quemSomos'),
    
    url(r'^admin', 'app.views.admin', name='admin'),    
    url(r'^prestadores', 'app.views.prestadores', name='prestadores'),
    url(r'^contratantes', 'app.views.contratantes', name='contratantes'),
    url(r'^relatorioAdm', 'app.views.relatorioAdm', name='relatorioAdm'),
    #Menu Prestador
    url(r'^cadPrestador', 'app.views.cadPrestador', name='cadPrestador'),    
    url(r'^servPrestados', 'app.views.servPrestados', name='servPrestados'),
    url(r'^colmeiaPontos', 'app.views.colmeiaPontos', name='colmeiaPontos'),
    url(r'^relPrestador', 'app.views.relPrestador', name='relPrestador'),
    #Menu Contratante
    url(r'^cadContratante', 'app.views.cadContratante', name='cadContratante'),    
    url(r'^servContratados', 'app.views.servContratados', name='servContratados'),
    url(r'^relContratante', 'app.views.relContratante', name='relContratante'),

    #Urls persistencia
    url(r'^i_prestador', p_usuario.incluirPrestador, name='i_prestador'),
    url(r'^i_contratante', p_usuario.incluirContratante, name='i_contratante'),
    url(r'^aprova_usuariosP', p_usuario.aprovaUsuarioP, name='aprova_usuariosP'),
    url(r'^aprova_usuariosC', p_usuario.aprovaUsuarioC, name='aprova_usuariosC'),
    #url(r'^sucesso', p_usuario.incluirContratante, name='i_contratante'),
    #url(r'^c_usuario', c_usuario.incluir, name='c_usuario'),

    #Site Principal
    url(r'^s_contato', 'app.views.s_contato', name='s_contato'),
    url(r'^s_quemSomos', 'app.views.s_quemSomos', name='s_quemSomos'),

    url(r'^sair', 'app.views.sair', name='sair'),
    url(r'^fazLogin', 'app.views.fazLogin', name='fazLogin'),
    
    url(r'^loginpage',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/geral/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Colmeia Login',
                'year':datetime.now().year,
            }
        },
        name='login'),
    
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
