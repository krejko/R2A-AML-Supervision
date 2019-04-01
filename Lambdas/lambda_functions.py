import pandas as pd
import numpy as np
import json
import sqlalchemy
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from datetime import datetime


def gnosis_tag(df, name_db):
	nm = []
	ps = []
	for i in len(df.index):
		nm.append(i)
		for y in len(df.columns):
			ps.append(y)
	db_positions = zip(nm,ps,name_db)
	db_pos_json = [json.dumps(db_positions[x]) for x in db_positions]
	df['gnosis_pos']= db_pos_json

	return df

def gnosis_look(df, json):
	looker = json.loads(json)
	looker = looker[-1]
	trace = df.loc[df['gnosis_pos']==looker]
	return trace


def check_token(token):
	#Load token from psql
	if token in tkn:
		return 'Correct Token'
	else
		return 'Incorrect Token, cannot continue'
		break

def validate(info):
	correct = np.zeros(len(type_list))
    incorrect = np.zeros(len(type_list))
    for x in range(dataframe.columns):
        if dataframe[[x]] is type_list[x]:
            correct[x] = 1
        else:
            print('Column {} is incorrect type'.format(x))
            incorrect[x] = 1
    return correct, incorrect

def return_pdf(token, file,df):
	fecha = datetime.now().date()
	#Load token from psql
	inst = df.loc[df['institucion']==token]
	c = canvas.Canvas('Acuse_Recibido_{}_{}_{}.pdf'.format(fecha, inst, file))
	c.showPage()
	c.save()
	return c


def accepted():
	if incorrect.shape == 0:
		return 'Accepted'
		return_pdf()
	else
		return 'Not accepted'
		rechazada()

def rechazada():
	return print('Information is not in the correct format')
	break
if __name__ == '__main__':
	main()