import pandas as pd
import matplotlib.pyplot as plt
import os

sciezkaDoDanych = os.path.join('..','TopBabyNamesbyState.csv')

df = pd.read_csv(sciezkaDoDanych)

#Wykres z liczbą przykładów dla Top 10 imion (odkomentowac jesli chce sie uzyc)
# df['Top Name'].value_counts().sort_values(ascending=False)[:10].plot(kind='bar')

# plt.ylabel('Liczba przykładów')
# plt.xlabel('')
# plt.title('Liczba przykładów dla Top 10 imion')
# plt.show()
