import pandas as pd
from data_Filtring import data_reading,data_filtring
from sklearn.preprocessing import LabelEncoder
import numpy as np
import sys
import yaml
import os
params = yaml.safe_load(open('params.yaml'))['features_extraction']

if len(sys.argv) !=2 :
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython prepare.py data-file\n")
    sys.exit(1)

deli =params['delimiter'] 
path = sys.argv[1]
output_train = os.path.join('data_', 'Output_features_extraction.csv')
def LabelEncoder_(data,column):
	label_encoder = LabelEncoder()
	encoding_vector= label_encoder.fit_transform(data[column])
	return encoding_vector
def number_cipher(list_ciphers):
    if 'nan' in list_ciphers:
        return 0
    else: 
        return len(list_ciphers)
def features_extract():
	#list_features = ["EXTENSIONS_SUPPORTED_GROUP", "HANDCIPHERSUITE", "HOST", "LENGTH_WINDOW_MAX", "LENGTH_WINDOW_MAX_OUT",
        #                       "PACKET_LENGTH_MAX_OUT", "SIGHASHSIG", "SIGHASHHASH", "LENGTH_WINDOW_MIN_OUT"]
	list_features = ["LENGTH_WINDOW_MAX","LENGHTWINDOW_OUT","LENGTH_WINDOW_EXT_OUT","PACKET_LENGTH_MAX","CAUTION_DF","PACKET_LENGTH_MIN_OUT","PACKET_LENGTH_EXT_OUT","TIMETOLIVE","PACKETLENGHT_OUT","RATIO_PACK_TRAFFIC","BPP","NON_FRAGMENTED","TOTAL_PACKET_LENGHT","NBR_PACKET_OUT","NBR_N_PACKETLENGHT","NBR_DF_PACKETLENGHT","NBR_PACKET","CAT_RATIO_PACK_TRAFFIC"]
	data = data_reading(path,deli)[:-1]
	data = data_filtring(data,list_features)
	data.to_csv(output_train)

features_extract()
