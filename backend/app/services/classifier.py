import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

from app.core.label_mapping import LABEL_MAP

MODEL_PATH = "trained_models/promptshield_distilbert"

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH
)

model.eval()


def classify_prompt(text: str):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

        probs = torch.softmax(
            outputs.logits,
            dim=1
        )

        confidence, prediction = torch.max(
            probs,
            dim=1
        )

    label = prediction.item()

    return {
        "label": label,
        "attack_type": LABEL_MAP[label],
        "confidence": float(confidence)
    }