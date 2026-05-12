import pandas as pd
import matplotlib.pyplot as plt
import os
import calcul
import intro

sciezkaDoDanych = os.path.join('..','TopBabyNamesbyState.csv')

df = pd.read_csv(sciezkaDoDanych)

#Wykres z liczbą przykładów dla Top 10 imion (odkomentowac jesli chce sie uzyc)
# df['Top Name'].value_counts().sort_values(ascending=False)[:10].plot(kind='bar')

# plt.ylabel('Liczba przykładów')
# plt.xlabel('')
# plt.title('Liczba przykładów dla Top 10 imion')
# plt.show()

def tabeleDlaKlastrów():
    for i in range(0,len(intro.zdenormalizowaneKlastryBezNrCentroid)):
        df = pd.DataFrame({"State": [], "Gender": [], "Year": [], "Top Name": [], "Occurences": []})
        nrKlastra = i
        print('')
        print('Tabela danych dla klastra', nrKlastra)
        for j in range(0,len(intro.zdenormalizowaneKlastryBezNrCentroid[i])):
            df.loc[len(df)] = intro.zdenormalizowaneKlastryBezNrCentroid[i][j]
        if df.empty:
            print('Brak danych w klastrze')
        else: print(df)
