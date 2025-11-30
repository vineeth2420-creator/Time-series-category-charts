import pandas as pd
import matplotlib.pyplot as plt

# 1. Read data
df = pd.read_csv("sales_data.csv")

# 2. Parse date column and sort
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

print(df.head())
# === Daily sales over time ===
daily_sales = df.groupby("Date")["Sales"].sum()

plt.figure()
daily_sales.plot(kind="line")
plt.title("Daily Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("daily_sales_line.png")
plt.close()
# === Monthly aggregation ===
df_monthly = df.set_index("Date").resample("M")["Sales"].sum()

plt.figure()
df_monthly.plot(kind="line")
plt.title("Monthly Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("monthly_sales_line.png")
plt.close()
# === Quarterly aggregation ===
df_quarterly = df.set_index("Date").resample("Q")["Sales"].sum()

plt.figure()
df_quarterly.plot(kind="line")
plt.title("Quarterly Sales Over Time")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("quarterly_sales_line.png")
plt.close()
# === Bar chart: total sales by category ===
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure()
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("category_sales_bar.png")
plt.close()
# === Pie chart: category share of total sales ===
plt.figure()
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Share of Total Sales")
plt.ylabel("")  # hide y-label
plt.tight_layout()
plt.savefig("category_sales_pie.png")
plt.close()