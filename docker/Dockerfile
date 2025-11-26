# ===================================
# Stage Base
# ===================================
FROM python:3.12-slim as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# ===================================
# Stage Development
# ===================================
FROM base as development

RUN apt-get update && apt-get install -y \
    git \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN chmod +x /app/docker/entrypoint.sh

CMD ["sh", "docker/entrypoint.sh"]

# ===================================
# Stage Production
# ===================================
FROM base as production

RUN groupadd -r appuser && useradd -r -g appuser appuser

COPY . .

RUN chown -R appuser:appuser /app

USER appuser

RUN chmod +x /app/docker/entrypoint.sh

CMD ["sh", "docker/entrypoint.sh"]
