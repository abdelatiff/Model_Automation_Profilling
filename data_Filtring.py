import numpy as np
import pandas as pd
def data_reading(path,deli):
	data = pd.read_csv(path,sep=deli)
	return data
def data_filtring(data,list_of_features):
	data_Browser = data[list_of_features]
	print(data_Browser.describe())
	return data_Browser
	
