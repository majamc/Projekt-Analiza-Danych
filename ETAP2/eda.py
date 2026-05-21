import pandas as pd
import matplotlib.pyplot as plt
import os
import intro
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv("HealthcareDataset.csv")

#liczba przykladow dla kazdego wieku 
#odkomentowac jesli chce sie uzyc
# plt.figure(figsize=(13, 6))
# df["Age"].value_counts().sort_index().plot(kind='bar')

# plt.ylabel('Liczba przykładów')
# plt.xlabel('')
# plt.title('Liczba przykładów dla każdego wieku')
# plt.show()

def tabeleDlaKlastrów():
    #wypisywanie klastrów w formie tabelek i wyświetlanie wykresów dla klastrów
    #odkomentowac 2 linijki ponizej jesli chce sie zobaczyc wykresy !!!
    # fig, axes = plt.subplots(2, 3, figsize=(14, 6))
    # axes = axes.flatten()
    #2 = wiersze, 3 = kolumny bo narazie dla 6 klastrów (przy innej ilosci klastrow zmienic bo inaczej sie wywlali blad)
    for i in range(0,len(intro.zdenormalizowaneKlastryBezNrCentroid)):
        df = pd.DataFrame({"Age": [], "Gender": [], "Medical Condition": [], "Medication": [], "Admission Type": []})
        nrKlastra = i
        print('')
        print('Tabela danych dla klastra', nrKlastra)
        for j in range(0,len(intro.zdenormalizowaneKlastryBezNrCentroid[i])):
            df.loc[len(df)] = intro.zdenormalizowaneKlastryBezNrCentroid[i][j]
        if df.empty:
            print('Brak danych w klastrze')
        else: 
            print(df)
            #odkomentowac tez te dwie linijki pod jesli chcesz zobaczyc wykresy
    #     tabelaScatterplot(df, i, axes)
    # plt.show()
    
def tabelaScatterplot(df, i, axes):
    #wykres rozrzutu dla wszystkich danych danego klastra
    sns.scatterplot(
        data=df,
        x='Age',
        y='Medical Condition',
        size='Admission Type',
        hue='Gender',
        style='Medication',
        ax=axes[i]
    )
    axes[i].set_title(f'Klaster {i}')

def optimise_k_means(max_k):
    #tworzymy tabele z danych znormalizowanych
    data = pd.DataFrame(
        intro.krotkiNormal,
        columns=[
            'Age',
            'Gender',
            'Medical Condition',
            'Medication',
            'Admission Type',
            'Cluster'
        ]
    )
    # usuwamy numer klastra bo nie jest cechą danych
    data = data.drop(columns=['Cluster'])
    means = []
    # bledyKlastrow = inertia(zazwyczaj tak nazywana),suma odległości punktów od centroidów
    bledyKlastrow = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )
        #uczenie modelu na danych
        kmeans.fit(data)
        means.append(k)
        bledyKlastrow.append(kmeans.inertia_)
    plt.figure(figsize=(10, 5))
    plt.plot(means, bledyKlastrow, 'o-')
    plt.xticks(means)
    plt.xlabel('Liczba klastrów (k)')
    plt.ylabel('Ilość błędów')
    plt.title('Metoda łokcia')
    plt.grid(True)
    plt.show()