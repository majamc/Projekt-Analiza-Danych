import pandas as pd
import matplotlib.pyplot as plt
import os
import intro
import seaborn as sns
from sklearn.cluster import KMeans

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
        #tabelaScatterplot(df, i, axes)
    #plt.show()

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
# podobno lepiej użyć tylko x, y, hue, ax dla przejrzystości

#obliczanie poprawnej ilości klastrów
def optimise_k_means(max_k):
    #tworzymy tabele z danych znormalizowanych
    data = pd.DataFrame(
        intro.krotkiNormal,
        columns=[
            'State',
            'Gender',
            'Year',
            'Top Name',
            'Occurences',
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
    plt.xlabel('Liczba klastrów (k)')
    plt.ylabel('Ilość błędów')
    plt.title('Metoda łokcia')
    plt.grid(True)
    plt.show()

#co robi funkcja optimise_k_means
# 1. próbuje różne liczby klastrów k
# 2. uruchamia dla nich algorytm K-Means
# 3. sprawdza, jak dobry jest podział danych
# 4. rysuje wykres
# 5. my wybieramy najlepsze k (te po którym wykres zmienia się najmniej)