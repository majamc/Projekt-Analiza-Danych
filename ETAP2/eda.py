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