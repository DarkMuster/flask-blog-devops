# Stage 1 — Builder
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --target=/app/packages

# Stage 2 — Production
FROM python:3.11-slim AS production

WORKDIR /app

# Create non-root user for security
RUN addgroup --system flask && \
    adduser --system --ingroup flask flask

# Copy installed packages from builder
COPY --from=builder /app/packages /app/packages

# Copy app code
COPY . .

# Set ownership
RUN chown -R flask:flask /app

# Switch to non-root user
USER flask

# Environment variables
ENV PYTHONPATH=/app/packages:$PYTHONPATH
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

EXPOSE 5000

CMD ["python", "run.py"]