# 🛡️ PromptShield Python SDK

Official Python SDK for interacting with PromptShield.

The SDK enables developers to:

- 🔍 Scan prompts for security threats
- 🤖 Send prompts through the PromptShield secure chat pipeline
- ❤️ Check PromptShield server health
- ⚙️ Configure providers and SDK behavior
- 🚀 Integrate PromptShield into any Python application

---

## Installation

```bash
pip install promptshield
```

## Quick Start

```python
from promptshield import PromptShield

shield = PromptShield()

response = shield.chat(
    "Explain Artificial Intelligence."
)

print(response.response)
```

---

## Features

- Prompt Injection Detection
- Jailbreak Detection
- PII Detection
- Prompt Sanitization
- Secure LLM Middleware
- Multi-Provider Support
- Response Guard
- Developer-Friendly Python SDK

---

## Examples

```bash
python examples/scan_example.py
python examples/chat_example.py
python examples/health_example.py
python examples/configuration_example.py
python examples/advanced_example.py
```