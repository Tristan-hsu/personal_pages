# syntax=docker/dockerfile:1
FROM python:3.11-slim

# --- Runtime basics --------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=7860 \
    # Flask will write the SQLite DB (or any runtime files) here
    FLASK_INSTANCE_PATH=/data/instance

# --- OS‑level dependencies -------------------------------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# --- Non‑root user ---------------------------------------------------------
# Hugging Face Spaces 會用 UID 1000 執行容器；我們用相同 UID 以
# 免權限問題（/data 與 /app 均對 1000:1000 可寫）。
RUN addgroup --gid 1000 appuser && \
    adduser  --uid 1000 --gid 1000 --disabled-password --gecos "" appuser

# --- Writable folders ------------------------------------------------------
RUN mkdir -p /app /data/instance && \
    chown -R appuser:appuser /app /data

WORKDIR /app

# --- Python dependencies ---------------------------------------------------
# 先複製 pyproject / requirements，以便利用 Docker layer cache。
COPY pyproject.toml ./

RUN pip install --no-cache-dir --upgrade pip && \
    # 你可以改成 `pip install .`，若依賴已列在 pyproject.toml
    pip install --no-cache-dir \
        email-validator==2.2.0 \
        flask-wtf==1.2.2 \
        flask==3.1.1 \
        flask-sqlalchemy==3.1.1 \
        gunicorn==23.0.0 \
        psycopg2-binary==2.9.10 \
        requests==2.32.4 \
        werkzeug==3.1.3 \
        sqlalchemy==2.0.41 \
        wtforms==3.2.1

# --- Application source ----------------------------------------------------
COPY . .

USER appuser

EXPOSE 7860

CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:app"]
