import pandas as pd
import os
import datetime
from SQLhelpers import * 
from bcb_tag import *
from bottle import Bottle, request, abort, response

import warnings
warnings.filterwarnings("ignore")

tokens = ["8938766c07a73db615bd7bc2a742547e",
          "38492732013ce3d629ac1d9b8a646e7a"]

apiRIPSin = Bottle()

@apiRIPSin.route('/api/rips_inusuales', method=['POST'])
def read_txt():
    
    #Determinando acceso
    datafile = request.files.get('datafile')
    pw = request.query.pw

    if pw not in tokens:
        return "TokenError: Acceso denegado, token no valido"

    if pw == "8938766c07a73db615bd7bc2a742547e":
        inst = "Banorte"
    else:
        inst = "Fondika"

    name, ext = os.path.splitext(datafile.filename)
    
    #Determinando si el archivo es valido
    if ext not in ('.txt'):
        return "FileError: Extension de archivo no permitida"

    now = datetime.datetime.now()
    save_path = "/tmp/fbd_rips_inusuales/{0}{1}{2}{3}{4}{5}{6}{7}".format(inst,now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)
    time = "{0}{1}{2}{3}{4}{5}{6}".format(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    #Guardando el archivo
    file_path = "{path}/{file}".format(path=save_path, file=datafile.filename)
    datafile.save(file_path)

    #get_postgres_connection()
    con = create_connection()

    df = pd.read_csv(file_path, encoding="ISO-8859-1", sep=";", header=None)

    if len(df.columns) is not 41:
        print("FileError: El Archivo {} no se encuentra en el formato especificado\n".format(datafile.filename))

    if df[0][0] == 1:
        return "FileError: El Archivo {} es de operaciones relevantes\n".format(datafile.filename)

    df = tag_gnosis(df,datafile.filename,time)

    df.to_sql('RepOperIn_{}_test'.format(inst),
              con,
              if_exists='append',
              index=False)

    #for c in df.columns:
        
    
    return '{} archivo listo en la base de datos.\n'.format(datafile.filename) 

if __name__ == '__main__':
    apiRIPSin.run( host='0.0.0.0', port=3000, reloader=True)
