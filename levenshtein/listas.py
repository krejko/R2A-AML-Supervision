# -*- coding: utf-8 -*-
import requests
from datetime import datetime
import sys
import io
import os
import subprocess
import shlex
import Levenshtein as Lv
import pandas as pd
import numpy as np
from time import sleep
import warnings
import xml.etree.ElementTree as ET
warnings.filterwarnings("ignore")


class XML2DataFrame:

    def __init__(self, xml_data):
        self.root = ET.XML(xml_data)

    def parse_root(self, root):
        return [self.parse_element(child) for child in iter(root)]

    def parse_element(self, element, parsed=None):
        if parsed is None:
            parsed = dict()
        for key in element.keys():
            parsed[key] = element.attrib.get(key)
        if element.text:
            parsed[element.tag] = element.text
        for child in list(element):
            self.parse_element(child, parsed)
        return parsed

    def process_data(self):
        structure_data = self.parse_root(self.root)
        return pd.DataFrame(structure_data)


def create_df():
    df = pd.DataFrame({'Campo': np.zeros(1),
                       'Nombre o razon social': np.zeros(1),
                       'RFC': np.zeros(1),
                       'Fecha de Nacimiento': np.zeros(1),
                       'Domicilio': np.zeros(1),
                       'Fecha de inclusion': np.zeros(1),
                       'Fecha de exclusion': np.zeros(1),
                       'Informacion': np.zeros(1),
                       'Apellidos o denominacion social': np.zeros(1),
                       'RFC con o sin homoclave': np.zeros(1),
                       'Año nac o const': np.zeros(1),
                       'Formato libre': np.zeros(1),
                       'Fecha completa': np.zeros(1),
                       'Fecha completa': np.zeros(1)
        })
    return df

def descarga_lista(url):
    colnames = [str(x) for x in range(0,12)]
    for x in range(len(url_ofac)):
        url = url_ofac[x]
        data = requests.get(url).content
        if (x == 0):
            texto_0 = pd.read_csv(io.StringIO(data.decode('utf-8')), names=colnames, header=None)
        else:
            texto_1 = pd.read_csv(io.StringIO(data.decode('utf-8')), names=colnames, header=None)
    
    return texto_0.head(), texto_1.head()



def lec_lista_ofac(url_ofac):
    nom_rfc = pd.read_csv('nombres_prueba.csv') 
    colnames = [str(x) for x in range(0,12)]
    for x in range(len(url_ofac)):
        url = url_ofac[x]
        data = requests.get(url).content
        if (x == 0):
            texto_0 = pd.read_csv(io.StringIO(data.decode('utf-8')), names=colnames, header=None)
            texto_0 = texto_0[:-2]
        else:
            texto_1 = pd.read_csv(io.StringIO(data.decode('utf-8')), names=colnames, header=None)
            texto_1 = texto_1[:-2]
    nom_rfc['similaridad']=['a' for i in range(len(nom_rfc['NOMBRE']))]
    nom_rfc['Nom Similar']=['a' for i in range(len(nom_rfc['NOMBRE']))]
    texto_p = nom_rfc
    for x in range(len(nom_rfc)):
        for y in range(len(texto_0)):
            if (Lv.ratio(texto_p['NOMBRE'][x], texto_0['3'][y]) > 0.8):
                texto_p['similaridad'][x] = Lv.ratio(texto_p['NOMBRE'][x], texto_0['3'][y])
                texto_p['Nom Similar'][x] = texto_0['3'][y]
                #texto_p.sort_values(by=texto_p.similaridad).reset_index(inplace=True)
    texto_p0 = nom_rfc
    for x in range(len(nom_rfc)):
        for y in range(len(texto_1)):
            if (Lv.ratio(texto_p0['NOMBRE'][x], texto_1['1'][y]) > 0.8):
                texto_p0['similaridad'][x] = Lv.ratio(texto_p0['NOMBRE'][x], texto_1['1'][y])
                texto_p0['Nom Similar'][x] = texto_1['1'][y]
                #texto_p0.sort_values(by=similaridad).reset_index(inplace=True)
    return texto_p, texto_p0

def lec_lista_onu(url_onu):
    url = url_onu
    xml_data = requests.get(url).content
    xml2df = XML2DataFrame(xml_data)
    texto_p = xml2df.process_data()
    nom_rfc = pd.read_csv('nombres_prueba.csv')

    nom_rfc['similaridad']=['a' for i in range(len(nom_rfc['NOMBRE']))]
    nom_rfc['Nom Similar']=['a' for i in range(len(nom_rfc['NOMBRE']))]

    texto_p0 = nom_rfc

    for x in range(len(nom_rfc['NOMBRE'])):
        for y in range(len(texto_p['FIRST_NAME'])):
            name = str(texto_p['FIRST_NAME'][y])+' '+str(texto_p['SECOND_NAME'][y])
            if (Lv.ratio(nom_rfc['NOMBRE'][x], name )> 0.8):
                texto_p0['similaridad'][x] =   Lv.ratio(nom_rfc['NOMBRE'][x], name )
                texto_p0['Nom Similar'][x]= nom_rfc['NOMBRE'][x]
#       for x in nom_rfc:
#        for y in texto_p:
#            if (Lv.ratio(nom_rfc['RFC'][x], texto_p['RFC'][y] )> 0.8):
#                texto_p['similaridad rfc'] =   Lv.ratio(nom_rfc['RFC'][x], texto_p['RFC'][y] )
#                texto_p['RFC Similar'] = nom_rfc['RFC'][x]
    return texto_p0


if __name__ == '__main__':
    url_ofac = ['https://www.treasury.gov/ofac/downloads/alt.csv','https://www.treasury.gov/ofac/downloads/sdn.csv']
    url_onu = 'https://scsanctions.un.org/resources/xml/en/consolidated.xml'
    #df = create_df()
    print('Leyendo Listas')
    ofac_alt, ofac_sdn = descarga_lista(url_ofac)
    sleep(10)
    print('Lista ofac alias primeros 5 renglones')
    print(ofac_alt)
    sleep(10)
    print('Lista ofac sdn primeros 5 renglones')
    print(ofac_sdn)
    sleep(10)
    print('Comparando listas')
    aaa,bbb =lec_lista_ofac(url_ofac)
    sleep(20)
    print('Matches lista ofac alias')
    print(aaa)
    sleep(20)
    print('Matches lista ofac sdn')
    print(bbb)

    