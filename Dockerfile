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

# Create a non-root user and set permissions
RUN adduser --system --group flaskuser && chown -R flaskuser:flaskuser /app
USER flaskuser

# Copy dependency definitions first
COPY pyproject.toml ./

# Install Python dependencies
USER root
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir \
        email-validator>=2.2.0 \
        flask-wtf>=1.2.2 \
        flask>=3.1.1 \
        flask-sqlalchemy>=3.1.1 \
        gunicorn>=23.0.0 \
        psycopg2-binary>=2.9.10 \
        requests>=2.32.4 \
        werkzeug>=3.1.3 \
        sqlalchemy>=2.0.41 \
        wtforms>=3.2.1
USER flaskuser

# Copy application code
COPY . .

ENV PORT=7860
ENV FLASK_INSTANCE_PATH=/app/instance
# Expose the default Hugging Face port
EXPOSE 7860

# Launch the application using gunicorn
CMD ["/bin/sh", "-c", "gunicorn --bind 0.0.0.0:$PORT --workers 1 app:app"]