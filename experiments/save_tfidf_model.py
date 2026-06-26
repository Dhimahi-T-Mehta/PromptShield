import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv(
    "../data/training/promptshield_master.csv"
)

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_vec, y)

joblib.dump(
    vectorizer,
    "../backend/trained_models/tfidf_vectorizer.pkl"
)

joblib.dump(
    model,
    "../backend/trained_models/tfidf_classifier.pkl"
)

print("Model saved successfully")