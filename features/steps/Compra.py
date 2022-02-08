from datetime import time
import time
from features import environment

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import environment

from behave import given, when, then  # do behave importe x, y, z
from selenium import *

# método executado antes da feature e serve para chamar os passos seguintes
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(
            #pode ser incluida outras açoes
        )


@given(u'que eu acesso o site Blazedemo')
def step_impl(context):
    context.driver.get('https://www.blazedemo.com')
    print('Passo 1 - Acessou o site blazedemo')
    time.sleep(5)  # remover sempre essa espera bruta


@when(u'seleciono a cidade de origem como "{origem}"')
def step_impl(context, origem):

    # Mapeia a lista das cidades de origem
    lista_origem = context.driver.find_element(By.NAME, 'fromPort')

    # Criar objeto para permitir selecionar as opçoes de origem na lista
    objeto_origem = Select(lista_origem)

    # Seleciona o elemento na lista
    objeto_origem.deselect_by_visible_text(origem)

    print('Passo 2 - Selecionou a cidade  de origem')


@when(u'seleciono a cidade de destino como "{destino}"')
def step_impl(context, destino):

    # Mapeia a lista das cidades de origem
    lista_destino = context.driver.find_element(By.NAME, 'toPort')

    # Criar objeto para permitir selecionar as opçoes de origem na lista
    objeto_destino = Select(lista_destino)

    # Seleciona o elemento na lista
    objeto_destino.deselect_by_visible_text(destino)

    print('Passo 3 - Selecionou a cidade de destino')


@when(u'clico em Find Flights')
def step_impl(context):
    print('Passo 4 - clico em Find Flights')


@then(u'sou direcionado para a pagina de selecao de voos')
def step_impl(context):
    print('Passo 5 - Direcionou para a pagina de selecao de voos')


@when(u'seleciono o primeiro voo')
def step_impl(context):
    print('Passo 6 - Selecionou o primeiro voo')


@then(u'sou direcionado para a pagina de pagamento')
def step_impl(context):
    print('Passo 7 - Direcionou para a pagina de pagamento')


@when(u'preencho os dados de pagamento')
def step_impl(context):
    print('Passo 8 - Preencheu os dados')


@when(u'clico no botao Purchase Flight')
def step_impl(context):
    print('Passo 9 - Clicou no botao Purchase Flight')


@then(u'sou direcionado para a pagina de confirmacao')
def step_impl(context):
    print('Passo 10 - Direcionou para a pagina de confirmação')


################################################################################
@given(u'que acesso o site Blazedemo')
def step_impl(context):
    print('Passo 1c - Acessou o site blazedemo')


@when(u'seleciono "São Paolo" para "Rome"')
def step_impl(context):
    print('Passo 2c - selecionou a origem e o destino')
