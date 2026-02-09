import psycopg2

def guardar_base(nombre, url, muestra):
    try:
        conn = psycopg2.connect(dbname= 'crypto', user='adrian', password = '12345678',host='localhost', port = '5432')
        cur = conn.cursor()
        
        cur.execute('''
            CREATE TABLE IF NOT EXISTS datos (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50),
                url TEXT,
                precio NUMERIC,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        cur.execute('''
        INSERT INTO datos(nombre, url,precio) 
        VALUES(%s, %s, %s)''', (nombre, url, muestra))

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f'No se pudo conectar a la base de datos, error {e}')



