from datasets import load_dataset
import pandas as pd

# ---------------------------
# Prompt Injection Dataset
# ---------------------------

prompt_ds = load_dataset(
    "deepset/prompt-injections"
)

rows = []

for sample in prompt_ds["train"]:
    label = sample["label"]

    rows.append({
        "text": sample["text"],
        "label": label,
        "attack_type":
            "safe" if label == 0
            else "prompt_injection"
    })

# ---------------------------
# Jailbreak Dataset
# ---------------------------

jailbreak_ds = load_dataset(
    "JailbreakBench/JBB-Behaviors",
    "behaviors"
)

for sample in jailbreak_ds["harmful"]:

    rows.append({
        "text": sample["Goal"],
        "label": 2,
        "attack_type": "jailbreak"
    })

for sample in jailbreak_ds["benign"]:

    rows.append({
        "text": sample["Goal"],
        "label": 0,
        "attack_type": "safe"
    })

# ---------------------------
# Custom Dataset
# ---------------------------

custom_df = pd.read_csv(
    "raw/custom_attacks.csv"
)

attack_map = {
    0: "safe",
    1: "prompt_injection",
    2: "jailbreak",
    3: "pii_extraction",
    4: "role_manipulation"
}

for _, row in custom_df.iterrows():

    rows.append({
        "text": row["text"],
        "label": row["label"],
        "attack_type":
            attack_map[row["label"]]
    })

# ---------------------------
# PII Dataset
# ---------------------------

pii_df = pd.read_csv(
    "raw/pii_dataset.csv"
)

for _, row in pii_df.iterrows():

    rows.append({
        "text": row["text"],
        "label": row["label"],
        "attack_type": row["attack_type"]
    })


# ---------------------------
# Role Manipulation Dataset
# ---------------------------

role_df = pd.read_csv(
    "raw/role_dataset.csv"
)

for _, row in role_df.iterrows():

    rows.append({
        "text": row["text"],
        "label": row["label"],
        "attack_type": row["attack_type"]
    })

# ---------------------------
# Save Dataset
# ---------------------------

master_df = pd.DataFrame(rows)

master_df.to_csv(
    "training/promptshield_master.csv",
    index=False
)

print(master_df.head())

print("\nTotal Samples:")
print(len(master_df))

print("\nClass Distribution:")
print(master_df["attack_type"].value_counts())