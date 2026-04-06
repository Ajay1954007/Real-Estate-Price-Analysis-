import pandas as pd

# 1. Load dataset
df = pd.read_csv(r"D:\Da Project\house_prices.csv")

# 2. Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")

# 3. Check columns
print("Columns:", df.columns)

# 4. Handle missing values
df["Price_in_rupees"] = pd.to_numeric(df["Price_in_rupees"], errors="coerce")
df["Price_in_rupees"] = df["Price_in_rupees"].fillna(df["Price_in_rupees"].mean())
df.dropna(subset=["location"], inplace=True)

# 5. Analyze prices per location
price_per_location = df.groupby("location")["Price_in_rupees"].mean()
print("\nPrice per location:\n", price_per_location)

# 6. Moving average
df["moving_avg"] = df["Price_in_rupees"].rolling(window=3, min_periods=1).mean()

# 7. Segmentation
df["segment"] = pd.cut(
    df["Price_in_rupees"],
    bins=[0, 5000000, 10000000, 50000000],
    labels=["Low", "Medium", "High"]
)

# 8. Demand trends
demand = df["location"].value_counts()
print("\nDemand trends:\n", demand)

# 9. Top locations
top_locations = df.groupby("location")["Price_in_rupees"].mean().sort_values(ascending=False).head(5)
print("\nTop locations:\n", top_locations)

# 10. Save cleaned dataset
df.to_excel(r"D:\Da Project\cleaned_house_prices.xlsx", index=False)

print("\nCleaned dataset saved successfully!")
