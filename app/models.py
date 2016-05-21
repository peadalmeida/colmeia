# -*- coding: utf-8 -*-
"""
Definition of models.
"""

from django.db import models
from django.forms import ModelForm
from django.conf import settings
import datetime
from django.contrib.auth.models import User
#Enumarator
TIPO_PESSOA = (('1',u'Pessoa Fisica'), ('2',u'Pessoa Juridica'))
ESTADOS =  (('AC', u'Acre'), ('AL', u'Alagoas'), ('AP',u'Amapa'), ('AM',u'Amazonas'),('BA',u'Bahia'),('CE',u'Ceara'), ('DF',u'Distrito Federal'), ('ES',u'Espirito Santo'),('GO',u'Goias'),('MA',u'Maranhao'),('MS',u'Mato Grosso do Sul'),('MT',u'Mato Grosso'),('MG',u'Minas Gerais'), ('PA',u'Para'),('PB',u'Paraiba'),('PR',u'Parana'),('PE',u'Pernambuco'),('PI',u'Piaui'),('RJ',u'Rio de Janeiro'),('RN',u'Rio Grande do Norte'),('RS',u'Rio Grande do Sul'),('RO',u'Rondonia'),('RR',u'Roraima'),('SC',u'Santa Catarina'),('SP',u'Sao Paulo'),('SE',u'Sergipe'),('TO',u'Tocantins'))

TIPO_SERVICO = (('1',u'Remunerada'), ('2',u'Voluntaria'), ('3',u'Remunerada e Voluntaria'))
DIA_SEMANA = (('1',u'Domingo'), ('2',u'Segunda-Feira'), ('3',u'Terca-Feira'), ('4',u'Quarta-Feira'), ('5',u'Quinta-Feira'), ('6',u'Sexta-Feira'), ('7',u'Sabado'))

#Classes
class Perfil(models.Model):
    IdentificadorPerfil = models.AutoField(primary_key = True)
    DescricaoPerfil = models.CharField(max_length = 50, null = False)
    DataHoraInclusao = models.DateTimeField(auto_now_add=True)
    DataHoraExclusao = models.DateTimeField(null = True)
    @classmethod
    def create(self,IdentificadorPerfil, DescricaoPerfil,DataHoraInclusao,DataHoraExclusao):
        objPerfil = Perfil(IdentificadorPerfil = IdentificadorPerfil, DescricaoPerfil = DescricaoPerfil,DataHoraInclusao = datetime.datetime.now(),DataHoraExclusao = null)
        return objPerfil

class Endereco(models.Model):
    IdentificadorEndereco = models.AutoField(primary_key = True)
    CEP = models.CharField(max_length = 8, null = False)
    Estado = models.CharField(choices=ESTADOS, max_length = 2, null = False)
    Cidade = models.CharField(max_length = 100, null = False)
    Bairro = models.CharField(max_length = 100, null = False)
    Logradouro = models.CharField(max_length = 100, null = False)
    Numero = models.IntegerField(verbose_name=u'Número')
    Complemento = models.CharField(max_length = 100, null = True)
    Latitude = models.CharField(max_length = 50, null = True)
    Longitude = models.CharField(max_length = 50, null = True)

    @classmethod
    def create(self,CEP,Estado, Cidade, Bairro, Logradouro, Numero, Complemento ):
        objEndereco = Endereco(CEP = CEP, Estado = Estado, Cidade = Cidade, Bairro = Bairro, Logradouro = Logradouro, Numero = Numero, Complemento = Complemento, Latitude = None, Longitude=None)
        return objEndereco



class Usuario(models.Model):
    #extende os atributos da tabela usuario com relacao 1 para 1
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    IdentificadorUsuario = models.AutoField(primary_key = True)
    IdentificadorPerfil = models.ForeignKey(Perfil)
    IdentificadorEndereco = models.ForeignKey(Endereco, null = True)
    IndicadorTipoPessoa = models.IntegerField(choices=TIPO_PESSOA, verbose_name='Tipo de Pessoa')
    CpfCnpj = models.CharField(max_length = 20, null = False, unique = True, verbose_name='CPF ou CNPJ')
    Nome = models.CharField(max_length = 100, null = False)
    Telefone1 = models.CharField(max_length = 16, null = True,verbose_name='Telefone Principal')
    Telefone2 = models.CharField(max_length = 16, null = True,verbose_name='Telefone Opcional')
    DataHoraAprovacao = models.DateTimeField(null = True)
    DataHoraInclusao = models.DateTimeField(auto_now_add=True)
    DataHoraExclusao = models.DateTimeField(null = True)

    @classmethod
    def create(self,IdentificadorEndereco, IdentificadorPerfil, IndicadorTipoPessoa,CpfCnpj,Nome,Telefone1,Telefone2,Email,Senha):
        user = User.objects.create_user(username = Email,
                                        first_name = Nome.split(' ')[0],
                                        password = Senha
                                        )
        user.is_active = False
        user.save()

        objUsuario = Usuario(user_id = user.id ,IdentificadorEndereco = IdentificadorEndereco, IdentificadorPerfil = IdentificadorPerfil ,IndicadorTipoPessoa = IndicadorTipoPessoa,CpfCnpj = CpfCnpj,Nome= Nome,Telefone1 = Telefone1,Telefone2 = Telefone2, DataHoraAprovacao = None, DataHoraInclusao = datetime.datetime.now(), DataHoraExclusao = None)
        return objUsuario

class TipoDiferencial(models.Model):
    IdentificadorTipoDiferencial = models.AutoField(primary_key = True)
    DescricaoTipoDiferencial = models.CharField(max_length = 100)

class Diferenciais(models.Model):
    IdentificadorDiferencial = models.AutoField(primary_key = True)
    IdentificadorUsuario = models.ForeignKey(Usuario)
    IndentificadorTipoDiferencial = models.ForeignKey(TipoDiferencial)
    Ano = models.IntegerField()
    TituloDiferencial = models.CharField(max_length = 50)
    DescricaoDiferencial = models.CharField(max_length = 150)
    DataHoraInclusao = models.DateTimeField(auto_now_add=True)
    DataHoraExclusao = models.DateTimeField(null = True)

class DisponibilidadeUsuario(models.Model):
    IdentificadorDisponibilidade =  models.AutoField(primary_key = True)
    IdentificadorUsuario =  models.ForeignKey(Usuario)
    IndicadorTipoDiponibilidade = models.IntegerField(choices=TIPO_SERVICO)
    DataHoraInclusao = models.DateTimeField(auto_now_add=True)
    DataHoraExclusao = models.DateTimeField(null = True)

class DisponibilidadeSemanal(models.Model):
    IdentificadorDisponibilidadeSemanal = models.AutoField(primary_key = True)
    DiaSemana = models.IntegerField(choices=DIA_SEMANA)

class DisponibilidadeDiaria(models.Model):
    IdentificadorDisponibilidadeDiaria = models.AutoField(primary_key = True)
    DataHoraInicio = models.DateTimeField()
    DataHoraFim = models.DateTimeField()

class DisponibilidadeHorario(models.Model):
    IdentificadorHorario = models.AutoField(primary_key = True)
    Hora = models.DateTimeField()

class HorarioSemana(models.Model):
    IdentificadorDisponibilidadeSemanal = models.ForeignKey(DisponibilidadeSemanal)
    IdentificadorHorario = models.ForeignKey(DisponibilidadeHorario)

class Categoria(models.Model):
    IdentificadorCategoria = models.AutoField(primary_key = True)
    DescricaoCategoria = models.CharField(max_length = 250)

class SubCategoria(models.Model):
    IdentificadorSubCategoria = models.AutoField(primary_key = True)
    DescricaoSubCategoria = models.CharField(max_length = 150)

class CategoriaSubCategoria(models.Model):
    IdentificadorSubCategoria = models.ForeignKey(SubCategoria)
    IdentificadorCategoria = models.ForeignKey(Categoria)

class Servico(models.Model):
    IdentificadorServico = models.AutoField(primary_key = True)
    IdentificadorCategoria = models.ForeignKey(Categoria)
    IdentificadorUsuario = models.ForeignKey(Usuario)
    IndicadorTipoServico = models.IntegerField(choices=TIPO_SERVICO)
    DescricaoServico = models.CharField(max_length = 100)
    ValorHora = models.DecimalField(max_digits=10, decimal_places=2)
    DataHoraInclusao = models.DateTimeField(auto_now_add=True)
    DataHoraExclusao = models.DateTimeField(null = True)

class ClienteServico(models.Model):
    IdentificadorClienteServico = models.AutoField(primary_key = True)
    IdentificadorUsuario = models.ForeignKey(Usuario)
    IdentificadorServico = models.ForeignKey(Servico)
    IdentificadorEndereco = models.ForeignKey(Endereco)
    DataServico = models.DateTimeField(null = True)
    DescricaoContratacao = models.CharField(max_length = 350)
    QuantidadeHoras = models.IntegerField()
    ValorTotalServico = models.DecimalField(max_digits=10, decimal_places=2)
    Avaliacao = models.IntegerField()
    DataHoraConfirmacao = models.DateTimeField(null = True)
    DataHoraInclusao = models.DateTimeField(auto_now_add=True)
    DataHoraExclusao = models.DateTimeField(null = True)
