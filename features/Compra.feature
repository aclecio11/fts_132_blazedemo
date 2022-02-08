@compra_passagem
Feature: Compra de Passagem Aerea
  # Descreve a compra pelo site blazedemo.com
  # E2E  =End to End = inicio ao fim
  Scenario: De Sao Paulo a Roma
    Given que eu acesso o site Blazedemo
    When seleciono a cidade de origem como "São Paolo"
    And seleciono a cidade de destino como "Rome"
    And clico em Find Flights
    Then sou direcionado para a pagina de selecao de voos
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados de pagamento
    And clico no botao Purchase Flight
    Then sou direcionado para a pagina de confirmacao


  Scenario: De Sao Paulo a Roma Compacto
    Given que acesso o site Blazedemo
    When seleciono "São Paolo" para "Rome"
    Then sou direcionado para a pagina de selecao de voos
    When seleciono o primeiro voo
    Then sou direcionado para a pagina de pagamento
    When preencho os dados de pagamento
    And clico no botao Purchase Flight
    Then sou direcionado para a pagina de confirmacao