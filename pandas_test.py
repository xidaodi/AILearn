import numpy as np
import pandas as pd

# create a pandas dataframe

arr=np.array([["Zhang",30,100],
             ["Chang",100,100],
             ["Huang",30,60]]
             )

df=pd.DataFrame(arr,index=[1,2,3],columns=["name","math","english"])

print(df)