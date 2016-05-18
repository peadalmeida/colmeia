
# -*- coding: utf-8 -*-
"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *

class BootstrapAuthenticationForm(AuthenticationForm):
    # Authentication form which uses boostrap CSS.
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['IndicadorTipoPessoa', 'CpfCnpj',
                  'Nome', 'Telefone1', 'Telefone2']

        widgets = {
            'IndicadorTipoPessoa': forms.Select(attrs={'class': 'form-control',
                                                       'placeholder': 'Tipo pessoa',
                                                       'required': 'true',
                                                       'style': 'margin-bottom: 10px; width: 200px;'
                                                       }),
            'CpfCnpj': forms.TextInput(attrs={'class': 'form-control',
                                              'style': 'margin-bottom: 10px; width: 200px;',
                                              'placeholder': 'CPF /  CNPJ',
                                              'title': '"Digite apenas números"',
                                              'required': 'true'}),

            'Nome': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Nome',
                                           'style': 'margin-bottom: 10px;',
                                           'required': 'true'}),

            'Telefone1': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Telefone',
                                                'style': 'margin-bottom: 10px; width: 200px;',
                                                'type': 'tel',
                                                'title': '"Digite apenas números"',
                                                'required': 'true'}),

            'Telefone2': forms.TextInput(attrs={'class': 'form-control',
                                                'type': 'tel',
                                                'style': 'margin-bottom: 10px; width: 200px;',
                                                'placeholder': 'Telefone',
                                                'title': '"Digite apenas números"'
                                                }),
        }

class UserForm(forms.Form):
    Email = forms.CharField(max_length=100, label=u'* E-mail',  widget=forms.TextInput({
        'class': 'form-control',
        'style': 'margin-bottom: 10px;',
        'type:': 'email',
        'required': 'required',
        'placeholder': 'E-mail',
        'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}',
        'title': 'Entre com um formato válido: exemplo@colmeia.com.br'
    }))
    Senha = forms.CharField(label=u'* Senha', max_length=100,  widget=forms.PasswordInput({
        'class': 'form-control',
        'required': 'required',
        'placeholder': 'Password'}))

class EnderecoForm(ModelForm):

    class Meta:
        model = Endereco

        fields = ['CEP', 'Estado', 'Cidade', 'Bairro',
                  'Logradouro', 'Numero', 'Complemento']

        widgets = {
            'CEP': forms.TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'CEP',
                                          'required': 'true',
                                          'style': 'margin-bottom: 10px; width: 200px;',
                                          'title': '"Digite apenas números"'
                                          }),
            'Estado': forms.Select(attrs={'class': 'form-control',
                                          'placeholder': 'Estado',
                                          'required': 'true',
                                          'style': 'margin-bottom: 10px; width: 200px;'
                                          }),
            'Cidade': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Cidade',
                                             'required': 'true',
                                             'style': 'margin-bottom: 10px;',
                                             'title': '"Digite apenas letras"'
                                             }),
            'Bairro': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Bairro',
                                             'required': 'true',
                                             'style': 'margin-bottom: 10px;',
                                             'title': '"Digite apenas letras"'
                                             }),
            'Logradouro': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Rua Exemplo ou Avenida Exemplo',
                                                 'required': 'true',
                                                 'style': 'margin-bottom: 10px;',
                                                 'title': '"Digite apenas letras"'
                                                 }),
            'Numero': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Numero',
                                             'required': 'true',
                                             'style': 'margin-bottom: 10px; width: 200px;',
                                             'title': '"Digite apenas números"'
                                             }),
            'Complemento': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Complemento',
                                                  'required': 'true',
                                                  'style': 'margin-bottom: 10px;'
                                                  })
        }
