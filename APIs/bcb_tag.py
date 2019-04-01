import json
import pandas as pd
import numpy as np


def tag_gnosis(df, name_db, time):
    tags = []
    for i in range(len(df.index)):
        tags.append('{"index":'+str(i)+',"file":"'+name_db+'","time":"'+time+'"}')
    
    db_pos_json = [json.dumps(x) for x in tags]
    df['gnosis_pos']= db_pos_json

    return df

def tag_gno_conc(df1, df2, name_df1, name_df2):
    nm = []
    ps = []
    for i in len(df1.index):
        nm.append(zip(df1['gnosis_pos'][i], df2['gnosis_pos'][i]))
        for y in len(df2.columns):
            ps.append(zip(df1['gnosis_pos'][y], df2['gnosis_pos'][y]))
    db_positions = zip(nm,ps,name_db)
    db_pos_json = [json.dumps(db_positions[x]) for x in db_positions]
    df1['gnosis_pos']= db_pos_json

    return df1
