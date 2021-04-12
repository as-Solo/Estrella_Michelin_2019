# Estas funciones están pensadas para poder devolver unos datos concretos de la web oficial de Estrella Michelín para aumentar el dataset
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re


def scrap_precio(web_michelin):
    '''
    Get the text into the li tag with class name = restaurant-details__heading-price
    Args:
        object dataframe value
    Returns:
        String
    '''
    web =  web_michelin
    html = requests.get(web)
    res = BeautifulSoup(html.content,"html.parser")

    precio = res.find_all('li', {'class' : 'restaurant-details__heading-price'})
    if len(precio) == 0:
        return 0
    cadena = precio[0].getText()
    cadena = cadena.replace('.', '')
    cadena = cadena.replace(',', '')

    texto = cadena

    patron_precio = "[\d]+"
    patron_moneda = "[A-Z]{3}"

    precios = re.findall(patron_precio, texto)
    moneda = re.findall(patron_moneda, texto)
    precios.append(moneda)
    return precios



def cambio_a_euro(datos):
    '''
    Get a especific kind of values and makes the proper conversion depends of the coin
    Args:
        object Dataframe value
    Retuns:
        list
    '''
    
    if datos == 0:
        return 0
    
    dict_cambios = {'EUR': 1, 'USD': 0.84,  'DKK': 0.13, 'HKD': 0.11, 'MOP': 0.11, 'KRW': 0.00075, 'SEK': 0.098, 'TWD': 0.03, 'GBP': 1.15}
    
    lista_euros = list()
    
    multiplicador = 1
    moneda = datos[-1][0]
    
    if len(datos) == 2:
        if moneda in dict_cambios:
            multiplicador = dict_cambios[moneda]
            lista_euros.append(round( float(datos[0]) * multiplicador, 2) )
    
    if len(datos) == 3:
        if moneda in dict_cambios:
            multiplicador = dict_cambios[moneda]
            dato_01 = (round( float(datos[0]) * multiplicador, 2) )
            dato_02 = (round( float(datos[1]) * multiplicador, 2) )
            lista_euros.append(dato_01)
            lista_euros.append(dato_02)
    
    return lista_euros




def media_precios(datos):
    '''
    Get one or two values and makes the mean
    Args:
        object Dataframe value
    Retuns:
        float
    '''
    
    if datos == 0:
        return 0
    
    if len(datos) == 1:
        return datos[0]
    
    if len(datos) == 2:
        return round( (datos[0] + datos[1]) / len(datos) ,2)




def scrap_telefono(web_michelin):
    '''
    Get the text into the span tag with class name =  flex-fill
    Args:
        object dataframe value
    Returns:
        String
    '''

    web =  web_michelin
    html = requests.get(web)
    res = BeautifulSoup(html.content,"html.parser")

    precio = res.find_all('span', {'class' : 'flex-fill'})
    if len(precio) == 0:
        return 'sin información'
    cadena = precio[0].getText()
    cadena = cadena.replace('.', '')
    cadena = cadena.replace(',', '')

    return cadena



def scrap_mail_propio(datos):
    '''
    Get the text into the div tag with class name = collapse__block-title d-flex
    Args:
        object dataframe value
    Returns:
        String
    '''
    web =  datos
    html = requests.get(web)
    res = BeautifulSoup(html.content,"html.parser")

    mail_propio = res.find_all('div', {'class' : 'collapse__block-title d-flex'})
    
    if len(mail_propio) == 0:
        return 'Sin información'

    mail_propio = str(mail_propio)

    pattern = '[w]{3}[.][a-z_-]+[.][a-z]+'

    respuesta =  re.findall(pattern, mail_propio)
    if len(respuesta) > 0:
        return respuesta[0]
    else:
        return 'Sin información'



def scrap_horarios(datos):
    '''
    Get the text into the div tag with class name = open__time-hour flex-fill
    Args:
        object dataframe value
    Returns:
        String
    '''
    try:
        web =  datos
        html = requests.get(web)
        res = BeautifulSoup(html.content,"html.parser")

        horario = res.find('div', {'class' : 'open__time-hour flex-fill'})

        if len(horario) == 0:
            return 'Sin información'

        return horario.getText().strip('\n')
    except:
        return 'Sin información'