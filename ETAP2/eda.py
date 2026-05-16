import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HealthcareDataset.csv")

#liczba przykladow dla kazdego wieku 
#odkomentowac jesli chce sie uzyc
# plt.figure(figsize=(13, 6))
# df["Age"].value_counts().sort_index().plot(kind='bar')

# plt.ylabel('Liczba przykładów')
# plt.xlabel('')
# plt.title('Liczba przykładów dla każdego wieku')
# plt.show()
