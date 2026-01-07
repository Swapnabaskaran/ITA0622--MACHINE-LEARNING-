
# Candidate Elimination Algorithm
import pandas as pd

data = [
['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
['Sunny','Warm','High','Strong','Warm','Same','Yes'],
['Rainy','Cold','High','Strong','Warm','Change','No'],
['Sunny','Warm','High','Strong','Cool','Change','Yes']
]

cols = ['Sky','Temp','Humidity','Wind','Water','Forecast','EnjoySport']
df = pd.DataFrame(data, columns=cols)

S = ['0']*(len(cols)-1)
G = [['?']*(len(cols)-1)]

for _,row in df.iterrows():
    if row[-1]=='Yes':
        for i in range(len(S)):
            if S[i]=='0': S[i]=row[i]
            elif S[i]!=row[i]: S[i]='?'
    else:
        G = [g for g in G if any(g[i]!=row[i] for i in range(len(S)))]

print("Specific Hypothesis:", S)
print("General Hypothesis:", G)
