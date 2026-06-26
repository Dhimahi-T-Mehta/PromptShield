import pandas as pd
from sklearn.model_selection import train_test_split

# Load master dataset
df = pd.read_csv(
    "training/promptshield_master.csv"
)

# Shuffle
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Split
train_df, test_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

# Save
train_df.to_csv(
    "training/train.csv",
    index=False
)

test_df.to_csv(
    "training/test.csv",
    index=False
)

print("Train Samples:", len(train_df))
print("Test Samples:", len(test_df))

print("\nTrain Distribution:")
print(train_df["attack_type"].value_counts())

print("\nTest Distribution:")
print(test_df["attack_type"].value_counts())