# ======================================================
# PromptShield Backend - Production Dockerfile
# ======================================================

FROM python:3.11-slim

# -----------------------------
# Environment
# -----------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# -----------------------------
# Working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Install required OS packages
# -----------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl && \
    rm -rf /var/lib/apt/lists/*

# -----------------------------
# Install Python dependencies
# -----------------------------
COPY requirements-prod.txt .

RUN pip install --no-cache-dir -r requirements-prod.txt

# -----------------------------
# Download spaCy model
# -----------------------------
RUN python -m spacy download en_core_web_lg

# -----------------------------
# Copy application
# -----------------------------
COPY . .

# -----------------------------
# Create non-root user
# -----------------------------
RUN useradd -m promptshield && \
    chown -R promptshield:promptshield /app

USER promptshield

# -----------------------------
# Health Check
# -----------------------------
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
CMD curl -f http://localhost:8000/docs || exit 1

# -----------------------------
# Expose API
# -----------------------------
EXPOSE 8000

# -----------------------------
# Start FastAPI
# -----------------------------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]