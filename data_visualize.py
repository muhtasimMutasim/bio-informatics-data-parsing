import pandas as pd
import numpy
from matplotlib import pyplot as plt
import requests


data_url = "https://raw.githubusercontent.com/muhtasimMutasim/bio-informatics-data-parsing/main/qiimedata/test.csv"
data_url_resp = requests.get( data_url )
data = data_url_resp.text.split("\n")

control5 = {}


for i in data:
    
    #print(i)
    data_set = i.split(",")
    name = data_set[0].strip()
    if name.strip() == "Sample" or i == "":
        continue
    #print(name)
    cntrl_5 = data_set[2].strip()
    control5[name] = cntrl_5
    
    
control5_list = sorted(control5.items())
x, y = zip(*control5_list)
plt.plot(x, y)
plt.show()
