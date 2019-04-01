import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import numpy.polynomial.polynomial as poly
import re
from sklearn.feature_extraction.text import TfidfVectorizer as TFIV
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
import itertools
import os
from datetime import date, timedelta
from sqlalchemy import create_engine

PG_USR = os.environ['PG_USR']
PG_HOST = os.environ['PG_HOST']
PG_PASS = os.environ['PG_PASS']
PG_DB = os.environ['PG_DB']

def califica(df,quants):
    df[[1]] = pd.cut(bins=quants,x=df[[3]],labels=False)+1
    return(df)

def train_rf(c_ini):
    dias = 45    

    fechaHasta = date.today()-timedelta(days=dias)
    fechaHasta = max(c_ini.fecha)-timedelta(days=dias)  

    train = datos[datos.fecha <= fechaHasta]
    test = datos[datos.fecha > fechaHasta]  

    train.reset_index(inplace=True)
    test.reset_index(inplace=True)  

    model_RF = RandomForestRegressor(n_estimators=150,oob_score=True,n_jobs=-1) 

    mod_RF = model_RF.fit(X,train[[1]])

    return mod_RF

def oord_json(mod_RF, c_ini):
    bbb = mod_RF.fit_transform(c_ini[[4]])

    return bbb
def get_postgres_connection():
    conn = psycopg2.connect(
        "dbname={} user={} password={} host={} port = {}".format(
            PG_DB, PG_USR,
            PG_PASS, PG_HOST, PG_PORT
        )
    )
    return conn


if __name__ == '__main__':
    con = get_postgres_connection()
    c_ini = pd.to_sql(name=['table_names'], con=con, index=False)
    c_ini = califica(c_ini, 10)
    mod = train_rf(c_ini)
    orden = oord_json(mod, c_ini)
