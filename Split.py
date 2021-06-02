import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
import sys
import yaml
import os
import random
params = yaml.safe_load(open('params.yaml'))['Split']

if len(sys.argv) !=3 :
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)
split = params['split']
random.seed(params['seed'])
X_train = os.path.join('data_Profiling','train' ,  'X_train.csv')
X_test = os.path.join('data_Profiling','test' , 'X_test.csv')
y_train = os.path.join('data_Profiling','train', 'y_train.csv')
y_test = os.path.join('data_Profiling', 'test', 'y_test.csv')
X_44=pd.read_csv(sys.argv[1])  # Features
y_44=pd.read_csv(sys.argv[2])
del X_44["Unnamed: 0"]
del y_44["Unnamed: 0"]
def data_spliting(X,y):	
	X_train4 ,X_test4, y_train4, y_test4 = train_test_split(X, y, test_size=split)
	X_train4.to_csv(X_train)
	X_test4.to_csv(X_test)
	y_train4.to_csv(y_train)
	y_test4.to_csv(y_test)
data_spliting(X_44,y_44)
