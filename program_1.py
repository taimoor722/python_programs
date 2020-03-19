import pandas as pd
import numpy as np
df=pd.DataFrame(data=np.random.randint(1,100,size=(300,5)))
print(df)
print(*df.columns.tolist(),'<= columns')
for i in df.columns:
    print(round(df.iloc[:,i].mean()),'is mean of column',i)
    
for i in df.columns:
    print(round(df.iloc[:,i].median()),'is median of column',i)

for i in df.columns:
    print(round(df.iloc[:,i].mode()),'is mode of column',i)
print('THE END')