from sklearn.ensemble import RandomForestClassifier
import sys
import os
import pickle
import numpy as np
import yaml
#import cPickle
import pandas as pd
import subprocess
params = yaml.safe_load(open('params.yaml'))['Modelling']

if len(sys.argv) !=3 :
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)

print(sys.argv[1])
X = pd.read_csv(sys.argv[1])
y = pd.read_csv(sys.argv[2])
print(y.head())
del y['Unnamed: 0']
print(X.head())
del X['Unnamed: 0']
max_depth = params['max_depth']
n_estimators = params['n_estimators']
min_samples_split = params['min_samples_split']
random_state = params['random_state']
subprocess.run(["mkdir", "Models"])
Models_dump = os.path.join('Models', 'profilling.pickle')
def train():
	clf4 = RandomForestClassifier(bootstrap=True, class_weight=None, criterion='entropy',
          	max_depth=max_depth, max_features='auto', max_leaf_nodes=None,
          	min_impurity_decrease=0.0, min_impurity_split=None,
          	min_samples_leaf=4, min_samples_split=min_samples_split,
          	min_weight_fraction_leaf=0.0, n_estimators=n_estimators, n_jobs=-1,
          	oob_score=False, random_state=random_state, verbose=0, warm_start=False)
	print(X.shape)
	print(y.shape)
	clf4.fit(X,y)
	with open(Models_dump,'wb') as f:
		pickle.dump(clf4, f)
train()
