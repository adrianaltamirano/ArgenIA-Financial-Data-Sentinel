''' 
    Creare una lista que contenga datos clave:valor que seran utiles para la representacion
    ordenada de datos e informacion simple para una Base de datos.
'''

def apis():
    APIS =[
        {'name': 'Dolar BLue',
        'fuente': 'https://api.bluelytics.com.ar/v2/latest',
        'price':['blue', 'value_avg']
        },
        {'name': 'Bitcoin',
        'fuente':'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,tether&vs_currencies=usd&include_24hr_change=true',
        'price': ['bitcoin', 'usd']
        },
        {'name': 'EUR/USD',
        'fuente': 'https://api.frankfurter.app/latest?from=USD&to=EUR',
        'price': ['rates', 'EUR']
        }
    ]
    return APIS 
apis()