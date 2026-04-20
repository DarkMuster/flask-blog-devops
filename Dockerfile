# Stage 1 — Builder
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --user -r requirements.txt

# Stage 2 — Production
FROM python:3.11-slim AS production

WORKDIR /app

# Create non-root user for security
RUN addgroup --system flask && \
    adduser --system --ingroup flask flask

# Copy installed packages from builder
COPY --from=builder /root/.local /home/flask/.local

# Copy app code
COPY . .

# Set ownership
RUN chown -R flask:flask /app

# Switch to non-root user
USER flask

# Environment variables
ENV PATH=/home/flask/.local/bin:$PATH
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

EXPOSE 5000

CMD ["python", "run.py"]
