
import pandas as pd

customers = pd.read_csv("customers.csv")
accounts = pd.read_csv("accounts.csv")
transactions = pd.read_csv("transactions.csv")


print("All three datasets loaded successfully!")

# about table shape

print("\nCUSTOMERS SHAPE:")
print(customers.shape)

print("\nACCOUNTS SHAPE:")
print(accounts.shape)

print("\nTRANSACTIONS SHAPE:")
print(transactions.shape)

# about table head

print("\nCUSTOMERS DATA:")
print(customers.head())

print("\nACCOUNTS DATA:")
print(accounts.head())

print("\nTRANSACTIONS DATA:")
print(transactions.head())

# about table information

print("\nCUSTOMERS INFORMATION:")
customers.info()

print("\nACCOUNTS INFORMATION:")
accounts.info()

print("\nTRANSACTIONS INFORMATION:")
transactions.info()

# about table summary

print("\nCUSTOMERS SUMMARY:")
print(customers.describe())

print("\nACCOUNTS SUMMARY:")
print(accounts.describe())

print("\nTRANSACTIONS SUMMARY:")
print(transactions.describe())

# Removing duplicates from the datasets

customers = customers.drop_duplicates()
print("Customer duplicates removed:", customers.duplicated().sum())

accounts = accounts.drop_duplicates()
print("Account duplicates removed:", accounts.duplicated().sum())

transactions = transactions.drop_duplicates()
print("Transaction duplicates removed:", transactions.duplicated().sum())


# CUSTOMERS DATA CLEANING

# Remove spaces

customers["name"] = customers["name"].str.strip()
customers["gender"] = customers["gender"].str.strip()
customers["city"] = customers["city"].str.strip()
customers["occupation"] = customers["occupation"].str.strip()
customers["segment"] = customers["segment"].str.strip()

# Convert join date into date format

customers["join_date"] = pd.to_datetime(
    customers["join_date"], format="mixed", errors="coerce"
)

# Replace invalid age 

customers.loc[
    (customers["age"] < 18) | (customers["age"] > 100), "age"
] = None

# Replace invalid income 

customers.loc[
    (customers["annual_income"] <= 0) |
    (customers["annual_income"] > 10000000),
    "annual_income"
] = None

# Fill missing value

customers["age"] = customers["age"].fillna(customers["age"].median())
customers["gender"] = customers["gender"].fillna("Unknown")
customers["occupation"] = customers["occupation"].fillna("Unknown")

customers["annual_income"] = customers["annual_income"].fillna(
    customers["annual_income"].median()
)

# Remove duplicate records

customers = customers.drop_duplicates()

print("\nCUSTOMER DATA CLEANING COMPLETED!")
print(customers.isnull().sum())


# ACCOUNTS DATA CLEANING

# Remove extra spaces

accounts["account_type"] = accounts["account_type"].str.strip()
accounts["branch"] = accounts["branch"].str.strip()

# Convert opening date into date format

accounts["opening_date"] = pd.to_datetime(
    accounts["opening_date"], format="mixed", errors="coerce"
)

# Replace invalid credit limit values

accounts.loc[accounts["credit_limit"] < 0, "credit_limit"] = None

# Remove duplicate records

accounts = accounts.drop_duplicates()

print("\nACCOUNT DATA CLEANING COMPLETED!")
print(accounts.isnull().sum())


# TRANSACTIONS DATA CLEANING

# Remove extra spaces

transactions["transaction_type"] = transactions["transaction_type"].str.strip()
transactions["status"] = transactions["status"].str.strip()
transactions["category"] = transactions["category"].str.strip()
transactions["merchant_name"] = transactions["merchant_name"].str.strip()
transactions["currency"] = transactions["currency"].str.strip()
transactions["payment_mode"] = transactions["payment_mode"].str.strip()
transactions["city"] = transactions["city"].str.strip()
transactions["transaction_time"] = transactions["transaction_time"].str.strip()

# Convert transaction date into date format

transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"], format="mixed", errors="coerce"
)

# Convert transaction amount into numeric format

transactions["amount"] = pd.to_numeric(
    transactions["amount"], errors="coerce"
)

# Check missing transaction amounts

print("\nMISSING TRANSACTION AMOUNTS:")
print(transactions["amount"].isnull().sum())

# Remove duplicate records

transactions = transactions.drop_duplicates()

print("\nTRANSACTION DATA CLEANING COMPLETED!")
print(transactions.isnull().sum())


# VERIFYING CLEANED DATA

print("\nCUSTOMERS DATA:")
print(customers.isnull().sum())
print("Duplicate records:", customers.duplicated().sum())

print("\nACCOUNTS DATA:")
print(accounts.isnull().sum())
print("Duplicate records:", accounts.duplicated().sum())

print("\nTRANSACTIONS DATA:")
print(transactions.isnull().sum())
print("Duplicate records:", transactions.duplicated().sum())

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")


# VERIFY CLEANED DATA TYPES

print("\nCUSTOMERS DATA TYPES:")
print(customers.dtypes)

print("\nACCOUNTS DATA TYPES:")
print(accounts.dtypes)

print("\nTRANSACTIONS DATA TYPES:")
print(transactions.dtypes)


# VERIFY DATE AND AMOUNT VALUES

print("\nCUSTOMER JOIN DATE CHECK:")
print(customers["join_date"].isnull().sum())

print("\nACCOUNT OPENING DATE CHECK:")
print(accounts["opening_date"].isnull().sum())

print("\nTRANSACTION DATE CHECK:")
print(transactions["transaction_date"].isnull().sum())

print("\nTRANSACTION AMOUNT CHECK:")
print(transactions["amount"].isnull().sum())

print("\nALL DATA CLEANING AND VERIFICATION STEPS COMPLETED!")

# MERGING CUSTOMERS AND ACCOUNTS

customer_accounts = pd.merge(
    customers,
    accounts,
    on="customer_id",
    how="left"
)

print("\nMERGED DATA:")
print(customer_accounts.head())

print("\nMERGED DATA SHAPE:")
print(customer_accounts.shape)

# MERGING TRANSACTIONS

final_data = pd.merge(
    customer_accounts,
    transactions,
    on="account_id",
    how="inner"
)

print("\nFINAL MERGED DATA:")
print(final_data.head())

print("\nFINAL DATA SHAPE:")
print(final_data.shape)