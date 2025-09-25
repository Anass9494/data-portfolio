import pandas as pd
import matplotlib.pyplot as plt

PRIMARY = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
MIRROR  = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

def load_owid_covid():
    for url in (MIRROR, PRIMARY):
        try:
            print(f"Trying: {url}")
            df = pd.read_csv(url)
            print("Loaded from:", url)
            return df
        except Exception as e:
            print("Failed:", e)
    raise RuntimeError("Could not load data.")

df = load_owid_covid()

# Clean
keep = ["iso_code","continent","location","date",
        "total_cases","new_cases","total_deaths","new_deaths",
        "people_vaccinated","people_fully_vaccinated","total_tests","population"]
df = df[keep]
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df.sort_values(['location','date'], inplace=True)

# Global daily cases
global_daily = df.groupby('date')['new_cases'].sum(min_count=1).fillna(0)

plt.figure(figsize=(10,5))
global_daily.plot()
plt.title("Global Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.tight_layout()
plt.savefig("covid_trends.png", dpi=150, bbox_inches="tight")
plt.show()
