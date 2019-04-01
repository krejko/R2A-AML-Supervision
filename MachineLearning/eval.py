import tensorflow as tf
import numpy as np
import pandas as pd
import os
import subprocess
import shlex
import re
import json
import sys
import io
import sklearn
from sklearn.externals import joblib

def eval(dataframe):
    data = dataframe
    sfww = subprocess.run([sys.executable, "classify.py", "-m", "~./matriz/neural_network.pb", "{}".format(data)], encoding="utf-8", stdout=subprocess.PIPE)
    sfww = sfww.stdout.splitlines()
    sfww = ' '.join(sfww)
    sc_sfw = re.compile(r'([0-9]+\.([0-9]+))')
    sc_sfw = re.findall(sc_sfw, sfww)
    a1, a2 = sc_sfw[0][0], sc_sfw[1][0]
    pink_ranger = json.dumps({
        "resultado": [{"a1": a1, "a2": a2}]
    })
    return pink_ranger
