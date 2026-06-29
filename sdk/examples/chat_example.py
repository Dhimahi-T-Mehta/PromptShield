from promptshield import PromptShield

shield = PromptShield()

response = shield.chat(
    "Explain Artificial Intelligence."
)

print(response.response)