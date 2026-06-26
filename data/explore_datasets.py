from datasets import load_dataset

print("=" * 60)
print("PROMPT INJECTION DATASET")
print("=" * 60)

prompt_ds = load_dataset("deepset/prompt-injections")

print("\nFeatures:")
print(prompt_ds["train"].features)

print("\nSample:")
print(prompt_ds["train"][0])

print("\nLabel Distribution (first 10 labels):")

for i in range(10):
    print(prompt_ds["train"][i]["label"])


print("\n\n" + "=" * 60)
print("JAILBREAK DATASET")
print("=" * 60)

jailbreak_ds = load_dataset(
    "JailbreakBench/JBB-Behaviors",
    "behaviors"
)

print("\nFeatures:")
print(jailbreak_ds["harmful"].features)

print("\nSample Harmful:")
print(jailbreak_ds["harmful"][0])

print("\nSample Benign:")
print(jailbreak_ds["benign"][0])