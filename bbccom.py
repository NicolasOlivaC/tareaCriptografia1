from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
import itertools
import re

#Configuraciones importantes
options = webdriver.ChromeOptions()
options.add_argument("--lang=en")
driver_path = './chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=options)
driver.maximize_window()

def miCuentaSect():
    driver.get('https://www.bbc.com/')
    driver.find_element_by_link_text('Sign in').click()
    driver.implicitly_wait(10)

def crearUsuario():
    miCuentaSect()
    driver.find_element_by_link_text('Register now').click()
    driver.implicitly_wait(10)
    #segundo paso
    time.sleep(3)
    driver.execute_script("document.getElementsByTagName('div')[14].remove()")
    driver.find_element_by_link_text('16 or over').click()
    #tercer paso
    driver.find_element_by_id('day-input').send_keys('01')
    driver.find_element_by_id('month-input').send_keys('01')
    driver.find_element_by_id('year-input').send_keys('1990')
    #cuarto paso
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "submit-button")))
    driver.execute_script("document.getElementsByTagName('div')[14].remove()")
    driver.find_element_by_id('submit-button').click()
    #quinto paso
    time.sleep(3)
    driver.find_element_by_id('user-identifier-input').send_keys(emailUser)
    driver.find_element_by_id('password-input').send_keys(passwordUser)
    driver.execute_script("document.getElementsByTagName('div')[14].remove()")
    driver.find_element_by_id('submit-button').click()
    #sexto paso...
    driver.find_element_by_xpath("//*[contains(text(), 'No, thanks')]").click()
    driver.find_element_by_id('submit-button').click()

def iniciarSesion():
    miCuentaSect()
    driver.find_element_by_id('user-identifier-input').send_keys(emailUser)
    driver.find_element_by_id('password-input').send_keys(passwordUser)
    driver.find_element_by_id('submit-button').click()

def restablerContrasena():
    miCuentaSect()
    driver.find_element_by_link_text('Need help signing in?').click()
    driver.find_element_by_link_text("I've forgotten my password").click()
    driver.find_element_by_id('user-identifier-input').send_keys(emailUser)
    driver.find_element_by_id('submit-button').click()

def modificarContrasena():
    iniciarSesion()
    #segundo paso
    driver.find_element_by_id('idcta-username').click()
    driver.find_element_by_link_text('Settings').click()
    driver.find_element_by_xpath("//a[@href='/account/settings/edit/password']").click()
    driver.find_element_by_id('current-password-input').send_keys(passwordUser)
    driver.find_element_by_id('new-password-input').send_keys(newPasswordUser)
    driver.find_element_by_xpath("//*[contains(text(), 'Save and continue')]").click()

def fuerzaBruta():
    diccionario = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    cantMinima = 8
    contador = 0
    miCuentaSect()
    driver.find_element_by_id('user-identifier-input').send_keys(emailUser)
    for tam in range (cantMinima, len(diccionario)):
        for password in itertools.product(diccionario, repeat=tam):
            if contador < 100:
                if(re.search('[A-Z]+[0-9]', ''.join(password)) ):
                    print('Intento numero:',contador+1, '- password:',password)
                    driver.find_element_by_id('password-input').clear()
                    driver.find_element_by_id('password-input').send_keys(password)
                    driver.find_element_by_id('submit-button').click()
                    contador += 1  
            else:
                break      
                    
########### CREDENCIALES USUARIO ###########
emailUser = 'emailpruebacripto@xedmi.com'
passwordUser = 'passwordprueba33'
newPasswordUser = 'passwordprueba22'

########### SELECCION DE ITEMS PEDIDOS ###########
# crearUsuario()
iniciarSesion()
# restablerContrasena()
# modificarContrasena()
# fuerzaBruta()