import pandas as pd
import os

sciezkaDoDanych = os.path.join('..','TopBabyNamesbyState.csv')

df = pd.read_csv(sciezkaDoDanych)

print(df.head())

print(df['Year'].sort_values(ascending=False).head())