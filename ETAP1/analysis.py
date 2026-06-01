import pandas as pd
import matplotlib.pyplot as plt
import intro
import seaborn as sns
from sklearn.cluster import KMeans

df = pd.read_csv('TopBabyNamesbyState.csv')

#Wykres z liczbą przykładów dla Top 10 imion (odkomentowac jesli chce sie uzyc)
# df['Top Name'].value_counts().sort_values(ascending=False)[:10].plot(kind='bar')

# plt.ylabel('Liczba przykładów')
# plt.xlabel('')
# plt.title('Liczba przykładów dla Top 10 imion')
# plt.show()

def tabeleDlaKlastrów():
    #wypisywanie klastrów w formie tabelek i wyświetlanie wykresów dla klastrów
    fig, axes = plt.subplots(2, 2, figsize=(15, 7)) #2 wiersze, 2 kolumny
    axes = axes.flatten()
    
    #wykres pomocniczy do wspólnej legendy dla wszystkich wykresów klastrów
    fig_tmp, ax_tmp = plt.subplots()
    tmp_df = pd.DataFrame(columns=["State", "Gender", "Year", "Top Name", "Occurences"])
    for cluster in intro.zdenormalizowaneKlastryBezNrCentroid:
        for row in cluster:
            tmp_df.loc[len(tmp_df)] = row
    all_states = sorted(tmp_df['State'].unique())
    all_genders = sorted(tmp_df['Gender'].unique())
    all_names = sorted(tmp_df['Top Name'].unique())
    sns.scatterplot(
        data=tmp_df,
        x='Occurences',
        y='Year',
        hue='State',
        style='Gender',
        size='Top Name',
        style_order=all_genders,
        hue_order=all_states,
        size_order=all_names,
        ax=ax_tmp
    )    
    handles, labels = ax_tmp.get_legend_handles_labels()
    plt.close(fig_tmp) #ukrycie pomocniczego wykresu
    
    dfCentroidy = pd.DataFrame(
        intro.zdenormalizowaneCentroidy,
        columns=[
            'State',
            'Gender',
            'Year',
            'Top Name',
            'Occurences'
        ]
    )
    
    for i in range(0,len(intro.zdenormalizowaneKlastryBezNrCentroid)):
        df = pd.DataFrame({"State": [], "Gender": [], "Year": [], "Top Name": [], "Occurences": []})
        centroida = dfCentroidy.iloc[[i]] #branie centroidy dla tego klastra
        print('')
        print('Tabela danych dla klastra', i)
        for j in range(0,len(intro.zdenormalizowaneKlastryBezNrCentroid[i])):
            df.loc[len(df)] = intro.zdenormalizowaneKlastryBezNrCentroid[i][j]
        if df.empty:
            print('Brak danych w klastrze')
        else: 
            print(df)
            tabelaScatterplot(df, i, axes, centroida)
    fig.legend( #dostosowanie legendy
        handles,
        labels,
        loc='lower center',
        bbox_to_anchor=(0.85, 0.05),
        ncol=4,
        fontsize=8
    )

    plt.tight_layout(rect=[0, 0, 0.7, 1]) #żeby się nie nachodziły napisy itp.
    plt.show()

def tabelaScatterplot(df, i, axes, centroida):
    #tworzy wykres rozrzutu dla wszystkich danych danego klastra
    all_states = sorted(df['State'].unique())
    all_genders = sorted(df['Gender'].unique())
    all_names = sorted(df['Top Name'].unique())
    sns.scatterplot(
        data=df,
        x='Occurences',
        y='Year',
        hue='State',
        style='Gender',
        size='Top Name',
        hue_order=all_states,
        style_order=all_genders,
        size_order=all_names,
        ax=axes[i],
        legend=False
    )
    sns.scatterplot(
        data=centroida,
        x='Occurences',
        y='Year',
        color='black',
        ax=axes[i],
        legend=False
    )
    axes[i].set_title(f'Klaster {i}')
    axes[i].set_ylabel("Rok")
    axes[i].set_xlabel("Liczba wystąpień")

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