import pandas as pd
import matplotlib.pyplot as plt
import os
import intro
import seaborn as sns

sciezkaDoDanych = os.path.join('..','TopBabyNamesbyState.csv')

df = pd.read_csv(sciezkaDoDanych)

#Wykres z liczbą przykładów dla Top 10 imion (odkomentowac jesli chce sie uzyc)
# df['Top Name'].value_counts().sort_values(ascending=False)[:10].plot(kind='bar')

# plt.ylabel('Liczba przykładów')
# plt.xlabel('')
# plt.title('Liczba przykładów dla Top 10 imion')
# plt.show()

def tabeleDlaKlastrów():
    fig, axes = plt.subplots(2, 3, figsize=(14, 6)) #2 = wiersze, 3 = kolumny bo narazie dla 6 klastrów (przy innej ilosci klastrow zmienic bo inaczej sie wywlali blad)
    axes = axes.flatten()
    for i in range(0,len(intro.zdenormalizowaneKlastryBezNrCentroid)):
        df = pd.DataFrame({"State": [], "Gender": [], "Year": [], "Top Name": [], "Occurences": []})
        nrKlastra = i
        print('')
        print('Tabela danych dla klastra', nrKlastra)
        for j in range(0,len(intro.zdenormalizowaneKlastryBezNrCentroid[i])):
            df.loc[len(df)] = intro.zdenormalizowaneKlastryBezNrCentroid[i][j]
        if df.empty:
            print('Brak danych w klastrze')
        else: 
            print(df)
            #odkomentowac te dwie linijki pod jesli chcesz zobaczyc wykresy
    #         tabelaScatterplot(df, i, axes)
    # plt.show()

#narazie zrobilam tak ale nwm czy to jest optymalne kiedy bedziemy miec wiecej danych i klastrow
#plus te legendy co znacza punkty sa strasznie duze i dlugie
def tabelaScatterplot(df, i, axes):
    #tworzy wykres rozrzutu dla wszystkich danych danej centroidy
    sns.scatterplot(
        data=df,
        x='Occurences',
        y='Year',
        size='State',
        hue='Gender',
        style='Top Name',
        ax=axes[i]
    )
    axes[i].set_title(f'Klaster {i}')