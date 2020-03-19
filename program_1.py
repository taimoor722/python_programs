import pandas as pd
import numpy as np
df=pd.DataFrame(data=np.random.randint(1,100,size=(300,5)))
print(df)
for i in df.columns:
    print(round(df.iloc[:,i].mean()),'is mean of column',i)