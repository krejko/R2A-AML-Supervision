import psycopg2
import sqlalchemy
import os

PG_HOST = os.environ['PG_HOST']
PG_USR = os.environ['PG_USR']
PG_PASS = os.environ['PG_PASS']
PG_DB = os.environ['PG_DB']
PG_PORT = os.environ['PG_PORT']

#Funcion para conectarse a la base de datos
def get_postgres_connection():
    con = psycopg2.connect(
        "dbname={} user={} password={} host={} port={}".format(
            PG_DB, PG_USR, PG_PASS,
            PG_HOST, PG_PORT
        )
    )
    return con

#Funcion para crear una conexion a la base de datos
def create_connection():
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(
        PG_USR,
        PG_PASS,
        PG_HOST,
        PG_PORT,
        PG_DB
    )
    return sqlalchemy.create_engine(url)