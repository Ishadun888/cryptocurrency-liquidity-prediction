import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load data
df = pd.read_csv('data/combined_coin_gecko_data.csv')

# Step 2: Display basic info
print("Initial shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

# Step 3: Drop rows with missing values (or handle differently if needed)
df.dropna(inplace=True)
print("After dropping NA rows:", df.shape)

# Step 4: Convert 'date' column to datetime (if exists)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

# Step 5: Select numerical columns to scale (exclude date or ID columns)
numeric_cols = df.select_dtypes(include='number').columns.tolist()
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Step 6: Save cleaned data
df.to_csv('data/cleaned_data.csv', index=False)
print("Preprocessing complete. Cleaned data saved to data/cleaned_data.csv")
