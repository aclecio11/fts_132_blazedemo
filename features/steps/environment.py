from selenium import webdriver

# Inicio
def before_all(context):    # Antes de tudo
    # Declarar o selenium, instanciar como navegador e apontar o driver
    context.driver = webdriver.Chrome('C:/Users/aclecio11/PycharmProjects/fts_132_blazedemo/drivers/chrome/97/chromedriver.exe')
    # Maximizar a janela do navegador
    context.driver.maximize_window()

    print('Passo A - antes de tudo')

# Fim
def after_all(context):     # Depois de tudo

    # Desligar / destruir o objeto do selenium
    context.driver.quit()

    print('Passo z - depois de tudo')