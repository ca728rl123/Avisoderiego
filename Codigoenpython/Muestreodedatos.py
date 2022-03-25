import pandas as pd
import math

wac = pd.read_excel("https://github.com/ca728rl123/IrrigacionAutomatica/blob/main/Codigoenpython/tabla%20de%20datos.xlsx?raw=true")
df = pd.DataFrame(wac)
 
print(df)

for p in range(50):
  p=int(input())
  print(df.iloc[0:p])
  break
