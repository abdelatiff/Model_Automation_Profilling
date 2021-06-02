import json
from pathlib import Path
import yaml
import sys
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,classification_report
import pandas as pd
import pickle
import os
from pathlib import Path
params = yaml.safe_load(open('params.yaml'))['evaluate']
repo_path = Path(__file__).parent.parent
if len(sys.argv) !=4 :
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)

X_test = pd.read_csv(sys.argv[1])
y_test = pd.read_csv(sys.argv[2])
del X_test['Unnamed: 0']
del y_test['Unnamed: 0']
with open(sys.argv[3],'rb') as mod:
	model = pickle.load(mod)
Metrics_path = os.path.join('Metrics', 'metrics.json')

def main(X_test,y_test,model):
	predictions = model.predict(X_test)
	accuracy = accuracy_score(y_test, predictions)
	#conf_matrics = confusion_to_json(confusion_matrix(predictions,y_test))
	#print(conf_matrics)
	#class_report = classification_report(y_test, predictions)
	#print(str(class_report))
	#print(pd.DataFrame(class_report))
	#"confusion_matrix":pd.DataFrame(conf_matrics)
	metrics = {"accuracy": accuracy}
	print(metrics)
	Metrics_path_conv = repo_path / Metrics_path
	print(Metrics_path_conv)
	Metrics_path_conv.write_text(json.dumps(metrics))

main(X_test,y_test,model)
