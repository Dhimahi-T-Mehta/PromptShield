from datasets import load_dataset

ds = load_dataset("deepset/prompt-injections")

for row in ds["train"]:
    if row["label"] == 1:
        print(row)
        break