import psycopg2
import pandas as pd


conn = psycopg2.connect(
    database='df0lvk81aft5pn',
    user='gykofakssthrut',
    password="027e02a54297ff707311d8a878d62c45fad5d709af2bd297cfd3b3dca9e17021",
    host="ec2-107-20-183-142.compute-1.amazonaws.com",
    port="5432")

cur = conn.cursor()

# df = pd.read_csv('Estrategias.csv', encoding='latin1')

# df.to_sql('Estrategias', conn, if_exists='append')

#
try:
    cur.execute('CREATE TABLE strategies (id serial PRIMARY KEY, nombre_de_la_estrategia varchar, descripcion varchar, \
temporalidad varchar, indicador1 varchar, parametros1 varchar, indicador2 varchar, parametros2 varchar, \
indicador3 varchar, parametros3 varchar, autor varchar, mercado_financiero varchar, tipo_de_estrategia varchar, \
condiciones_de_compra varchar, condiciones_de_venta varchar, stop_loss varchar, position_size varchar);')
# #
#     cur.execute('SELECT * FROM strategies;')
#     cur.execute('DROP TABLE strategies;') #eliminar tabla

# upload csv

    # cur.execute("SELECT * FROM strategies;")

    # colnames = [desc[0] for desc in cur.description]
    # print(colnames)

    # with open('Estrategias.csv', 'r') as f:
    #
    #     next(f)  # Skip the header row.
    #     cur.copy_from(f, 'strategies', sep=',')
    #
    # while True:
    #
    #     row = cur.fetchone()
    #     if row is None:
    #         break
    #
    #     print(row)
except Exception as e:
    print("I can't drop our test database!", e)

conn.commit()
conn.close()
cur.close()