
# FIND-S Algorithm
import pandas as pd

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No'],
    ['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

cols = ['Sky','Temp','Humidity','Wind','Water','Forecast','EnjoySport']
df = pd.DataFrame(data, columns=cols)

hypothesis = ['0'] * (len(cols)-1)

for i in range(len(df)):
    if df.iloc[i,-1] == 'Yes':
        for j in range(len(hypothesis)):
            if hypothesis[j] == '0':
                hypothesis[j] = df.iloc[i,j]
            elif hypothesis[j] != df.iloc[i,j]:
                hypothesis[j] = '?'

print("Final Hypothesis:", hypothesis)
