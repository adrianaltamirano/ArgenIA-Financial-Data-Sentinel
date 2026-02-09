import requests
import json
import apis_configuracion
import bd

def obtener_datos(url, nombre_dato):
  
        #Comprobamos correctamete la respuesta del servidor para proceder.
        #Guardamos en la variable "datos" los datos de la url e formato JSON y procedemos en otra bariable indagar especificamente
        #un dato ya conocido, teniendo en cuenta que JSON tiene la estructuca clave-valor, asi que accedemos de esa manera.
    datos = None
    try:
        response = requests.get(url, timeout=5) #tiempo de espera del servidor
        response.raise_for_status() #Error si la respuesta del servidor es diferente a 200
        if response:
            datos = response.json()
    except requests.exceptions.HTTPError as http_err: #ERrores de htpp especificos
        print(f"Error en el servidor! {nombre_dato}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error de conexion, verificar {nombre_dato}")

    return datos

def diccionario(json_diccionario, valores_diccionarios):
    '''
    Creamos una lupa ue accedera a los valores mas especificos dentro de los
    diccionarios.
    '''
    datos = json_diccionario #Acceso al JSON complrto, esto me da los

    for i in valores_diccionarios: #Accedemos 'valores' en 'Blue y value_avg'
        datos = datos[i]

    return datos


def main():
    json = apis_configuracion.apis()

    for i in json:
        comprobar = obtener_datos(i['fuente'], i['name'])

        if comprobar:
            nombre = i['name']
            url = i['fuente']
            muestra = diccionario(comprobar, i['price'])
            print(f'Procesando {nombre}: {muestra}.')
            bd.guardar_base(nombre, url, muestra)
        else:
            print('ERROR, comprobar.')
main()
