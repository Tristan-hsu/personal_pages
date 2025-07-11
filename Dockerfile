FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable stdout/stderr flushing
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create a non-root user and set permissions for /app
RUN adduser --system --group flaskuser && chown -R flaskuser:flaskuser /app

USER flaskuser

# Copy dependency definitions first
COPY pyproject.toml ./
COPY uv.lock ./

# Copy application code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir uv \
    && uv pip install --no-cache-dir -r uv.lock

ENV FLASK_INSTANCE_PATH=/app/instance

ENV PORT=7860
# Expose the default Hugging Face port
EXPOSE 7860

# Launch the application using gunicorn
CMD ["/bin/sh", "-c", "gunicorn --bind 0.0.0.0:$PORT --workers 1 app:app"]