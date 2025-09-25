import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

print(df.head())
