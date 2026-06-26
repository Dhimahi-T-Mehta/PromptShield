import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report
)

# Load dataset
df = pd.read_csv(
    "../data/training/promptshield_master.csv"
)

# Features and labels
X = df["text"]
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TF-IDF
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

X_train_vec = vectorizer.fit_transform(
    X_train
)

X_test_vec = vectorizer.transform(
    X_test
)

# Logistic Regression
model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train_vec,
    y_train
)

# Predictions
predictions = model.predict(
    X_test_vec
)

# Metrics
accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nAccuracy:")
print(round(accuracy * 100, 2), "%")

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        predictions
    )
)