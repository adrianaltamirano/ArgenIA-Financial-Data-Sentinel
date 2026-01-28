import requests
import json

def obtener_datos():
    url = 'https://criptoya.com/api/dolar'

    #Response es el objeto que obtiene los datos de la url
    response = requests.get(url)

    ''' Comprobamos correctamete la respuesta del servidor para proceder.
        GUardamos en la variable "datos" los datos de la url e formato JSON y procedemos en otra bariable indagar especificamente
        un dato ya conocido, teniendo en cuenta que JSON tiene la estructuca clave-valor, asi que accedemos de esa manera.
    '''
    if response.status_code == 200:
        datos = response.json()
        
        #No podemos mostrar los datos del JSON Juntos, hay que mostrarlo individualmente.
        campos_interes = ['ask', 'bid', 'timestamp']
        for i in campos_interes:
            print(f"{i}: {datos['ahorro'][i]}")
    else:
        print("ERROR, verificar")

    return response.text


obtener_datos()

