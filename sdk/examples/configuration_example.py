from promptshield import PromptShield
from promptshield import PromptShieldConfig

config = PromptShieldConfig(
    provider="gemini",
    timeout=120,
)

shield = PromptShield(config)

response = shield.chat(
    "Explain Machine Learning."
)

print(response.response)