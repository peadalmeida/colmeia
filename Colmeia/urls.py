"""
Definition of urls for Colmeia.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

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
                       url(r'^prestadores', 'app.views.prestadores',
                           name='prestadores'),
                       url(r'^contratantes', 'app.views.contratantes',
                           name='contratantes'),
                       url(r'^relatorioAdm', 'app.views.relatorioAdm',
                           name='relatorioAdm'),
                       # Menu Prestador
                       url(r'^cadPrestador', 'app.views.cadPrestador',
                           name='cadPrestador'),
                       url(r'^servPrestados', 'app.views.servPrestados',
                           name='servPrestados'),
                       url(r'^colmeiaPontos', 'app.views.colmeiaPontos',
                           name='colmeiaPontos'),
                       # Menu Prestador
                       url(r'^cadContratante', 'app.views.cadContratante',
                           name='cadContratante'),
                       url(r'^servContratados', 'app.views.servContratados',
                           name='servContratados'),
                       url(r'^relContratante', 'app.views.relContratante',
                           name='relContratante'),

                       # Site Principal
                       url(r'^s_contato', 'app.views.s_contato', name='s_contato'),
                       url(r'^s_quemSomos', 'app.views.s_quemSomos',
                           name='s_quemSomos'),

                       url(r'^sair', 'app.views.index', name='sair'),
                       url(r'^login',
                           'django.contrib.auth.views.login',
                           {
                               'template_name': 'app/geral/login.html',
                               'authentication_form': BootstrapAuthenticationForm,
                               'extra_context':
                               {
                                   'title': 'Colmeia Login',
                                   'year': datetime.now().year,
                               }
                           },
                           name='login'),
                       url(r'^logout$',
                           'django.contrib.auth.views.logout',
                           {
                               'next_page': '/',
                           },
                           name='logout'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       # url(r'^admin/', include(admin.site.urls)),
                       )
