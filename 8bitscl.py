from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import itertools

#Configuraciones importantes
options = webdriver.ChromeOptions()
driver_path = './chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=options)
driver.maximize_window()

def miCuentaSect():
    driver.get('https://www.8-bits.cl/')
    driver.find_element_by_link_text('Mi Cuenta').click()

def crearUsuario():
    driver.get('https://www.8-bits.cl/')
    driver.find_element_by_link_text('Crear Cuenta').click()
    #Campos que se deben rellenar para Signup
    driver.find_element_by_name('firstname').send_keys(firstname)
    driver.find_element_by_name('lastname').send_keys(lastname)
    driver.find_element_by_id('input-email').send_keys(emailUser)
    driver.find_element_by_name('telephone').send_keys(telephone)
    driver.find_element_by_name('address_1').send_keys(addres)
    driver.find_element_by_name('city').send_keys(city)
    seleccion2 = Select(driver.find_element_by_name('zone_id'))
    seleccion2.select_by_value('4')
    driver.find_element_by_id('input-password').send_keys(passwordUser)
    driver.find_element_by_id('input-confirm').send_keys(passwordUser)
    driver.find_element_by_name('agree').click()
    driver.find_element_by_css_selector("[value^='Continuar']").click()

def iniciarSesion():
    miCuentaSect()
    driver.find_element_by_id('input-email').send_keys(emailUser)
    driver.find_element_by_id('input-password').send_keys(passwordUser)
    driver.find_element_by_css_selector("[value^='Acceder']").click()

def restablecerContrasena():
    miCuentaSect()
    driver.find_element_by_link_text('Recordar la contraseña').click()
    driver.find_element_by_id('input-email').send_keys(emailUser)
    driver.find_element_by_css_selector("[value^='Continuar']").click()

def modificarContrasena():
    iniciarSesion()
    driver.find_element_by_link_text('Cambiar la contraseña').click()
    driver.find_element_by_id('input-password').send_keys(newPasswordUser)
    driver.find_element_by_id('input-confirm').send_keys(newPasswordUser)
    driver.find_element_by_css_selector("[value^='Continuar']").click()

def fuerzaBruta():
    diccionario = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    cantMinima = 4
    contador = 0
    miCuentaSect()
    driver.find_element_by_id('input-email').send_keys(emailUser)
    for tam in range (cantMinima, len(diccionario)):
        for password in itertools.product(diccionario, repeat=tam):
            if contador <= 100:
                print('Intento numero:',contador+1, '- password:',password)
                driver.find_element_by_id('input-password').clear()
                
                driver.find_element_by_id('input-password').send_keys(password)
                driver.find_element_by_css_selector("[value^='Acceder']").click()
            else:
                break                
            contador += 1

def reseteoPassword10veces():
    miCuentaSect()
    for i in range(10):
        print("intento numero ", i+1)
        driver.find_element_by_link_text('Recordar la contraseña').click()
        driver.find_element_by_id('input-email').send_keys(emailUser)
        driver.find_element_by_css_selector("[value^='Continuar']").click()

########### CREDENCIALES USUARIO ###########
emailUser = 'emailpruebacripto@xedmi.com'
passwordUser = 'passwordprueba33'
firstname = 'nombrePrueba'
lastname = 'apellidoPrueba'
email = 'emailPrueba3@gmail.com'
telephone = '999999999'
addres = 'direccionPrueba'
city = 'ciudadPrueba'
newPasswordUser = 'passwordprueba33'

########### SELECCION DE ITEMS PEDIDOS ###########
# crearUsuario()
iniciarSesion()
# restablecerContrasena()
# modificarContrasena()
# fuerzaBruta()
# reseteoPassword10veces()