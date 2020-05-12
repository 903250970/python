import pandas as pd
import os

data=pd.DataFrame()
# dir="D:/excel/"
filenames=os.listdir(dir)

for name in filenames:
    print(name)
    data=pd.concat(data,name)

data
# data.to-exec("D:/789.xlsx")
