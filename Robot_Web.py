import pandas
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

excel_credenciales = r'C:\xampp\htdocs\Python\Accesos\Ejemplo.xlsx'
df = pandas.read.excel(excel_credenciales)

user = df['usuario'][0]
psw = df['contraseña'][0]
url = 'https://www.linkedin.com'

# Selectores:
boton_inicio_sesion = 'body > nav > a.nav_button-secondary'
selector_usuario = '#username'
selector_contraseña = '#password'
boton_login = '#app_container > main > div:nth-child(2) > form > div.login_form_action_container > button'

# Abrir Navegador
driver = webdriver.Chrome()
# Maximizar Pantalla
driver.maximize_window()
driver.get(url)

# Acciones de la página
driver.find_element_by_css_selector(boton_inicio_sesion).click()

# Loogearnos:
driver.find_element_by_css_selector(selector_usuario).send_keys(user)
driver.find_element_by_css_selector(selector_contraseña).send_keys(psw)
driver.find_element_by_css_selector(boton_login).click()

# Mas acciones dentro de la Página
time.sleep(7)
# Cerrar:
driver.quit()