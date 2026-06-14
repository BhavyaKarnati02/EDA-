import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("datasets/layoffs.csv")

print("Shape:")
print(df.shape)

print("\nInfo:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


plt.figure(figsize=(8,5))

df["total_laid_off"].hist(bins=30)

plt.title("Distribution of Total Layoffs")
plt.xlabel("Employees Laid Off")
plt.ylabel("Frequency")

plt.savefig("images/distribution_layoffs.png")

plt.show()

import seaborn as sns

plt.figure(figsize=(8,6))

sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True
)

plt.title("Correlation Heatmap")

plt.savefig("images/correlation_heatmap.png")

plt.show()

# Top 10 Companies by Layoffs

top_companies = (
    df.groupby("company")["total_laid_off"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

top_companies.plot(kind="barh")

plt.title("Top 10 Companies by Layoffs")
plt.xlabel("Total Laid Off")

plt.tight_layout()

plt.savefig("images/top_companies.png")

plt.close()
# Top 10 Countries by Layoffs

top_countries = (
    df.groupby("country")["total_laid_off"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))

top_countries.plot(kind="barh")

plt.title("Top 10 Countries by Layoffs")
plt.xlabel("Total Laid Off")

plt.tight_layout()

plt.savefig("images/top_countries.png")

plt.close()