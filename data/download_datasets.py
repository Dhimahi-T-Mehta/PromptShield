from datasets import load_dataset

print("Downloading Prompt Injection Dataset...")

prompt_ds = load_dataset(
    "deepset/prompt-injections"
)

print(prompt_ds)

print("\nDownloading Jailbreak Dataset...")

jailbreak_ds = load_dataset(
    "JailbreakBench/JBB-Behaviors",
    "behaviors"
)

print(jailbreak_ds)