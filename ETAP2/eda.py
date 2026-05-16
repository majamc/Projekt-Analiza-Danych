import pandas as pd

df = pd.read_csv("HealthcareDataset.csv")

print(df["Gender"].value_counts())
