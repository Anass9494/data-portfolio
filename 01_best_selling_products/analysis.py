import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales.csv", sep=";")
df.columns = df.columns.str.strip().str.lower()

# Group by product and sum quantities
totals = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
print(totals)

# Plot bar chart (single plot, default colors)
plt.figure(figsize=(8, 6))
totals.plot(kind="bar")
plt.title("Best-Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save
plt.savefig("best_selling_chart.png", dpi=150, bbox_inches="tight")
plt.savefig("best_selling_chart.svg", bbox_inches="tight")
plt.show()
