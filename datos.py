import requests
import json
from datetime import datetime

def obtener_datos():
    url = 'https://criptoya.com/api/dolar'

    #Response es el objeto que obtiene los datos de la url
    response = requests.get(url)

    ''' Comprobamos correctamete la respuesta del servidor para proceder.
        Guardamos en la variable "datos" los datos de la url e formato JSON y procedemos en otra bariable indagar especificamente
        un dato ya conocido, teniendo en cuenta que JSON tiene la estructuca clave-valor, asi que accedemos de esa manera.
    '''
    if response.status_code == 200:
        datos = response.json()

    return datos

def crear_diccionario(datos):
    Fecha = datetime.fromtimestamp(datos['blue']['timestamp']).strftime('%Y,%B,%d,%H,%M,%S')

    
    mensaje = {
        "FECHA": Fecha,
        "blue": float(datos['blue']['ask']),
        "cripto": float(datos['cripto']['ccb']['ask']),
        "mep": float(datos['mep']['al30']['24hs']['price'])
    }
    brecha = ((mensaje['blue'] / mensaje['mep']) -1) * 100

    informe =(f"/************************/ \n" 
        f"EL valor del Dolar BLue es :{mensaje['blue']}\n" 
        f"El valor del Dolar mep es :{mensaje['mep'] }\n"
        f"LA BRECHA ESTIMADA ES: {brecha:.2f}\n"
        f"/*************************/")
    return informe

def main():
    datos = obtener_datos()

    if datos:
        diccionario = crear_diccionario(datos)

        print(diccionario)
    else:
        print('No hay datos por ahora')


main()

