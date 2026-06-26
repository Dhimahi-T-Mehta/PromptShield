import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("../data/training/promptshield_master.csv")

# Rule-based classifier
def predict(text):

    text = str(text).lower()

    # Prompt Injection
    if (
        "ignore previous" in text
        or "forget previous" in text
        or "system prompt" in text
        or "show me your prompt" in text
    ):
        return 1

    # Jailbreak
    elif (
        "dan" in text
        or "developer mode" in text
        or "unrestricted ai" in text
    ):
        return 2

    # PII
    elif (
        "email" in text
        or "phone number" in text
        or "aadhaar" in text
        or "pan" in text
        or "customer database" in text
    ):
        return 3

    # Role Manipulation
    elif (
        "act as" in text
        or "pretend to be" in text
        or "root user" in text
        or "administrator" in text
    ):
        return 4

    return 0


# Predictions
df["prediction"] = df["text"].apply(predict)

# Accuracy
accuracy = accuracy_score(
    df["label"],
    df["prediction"]
)

print("\nAccuracy:")
print(round(accuracy * 100, 2), "%")

print("\nClassification Report:\n")

print(
    classification_report(
        df["label"],
        df["prediction"]
    )
)