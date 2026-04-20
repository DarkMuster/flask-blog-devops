# Stage 1 — Builder
FROM python:3.11-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Stage 2 — Production
FROM python:3.11-slim AS production

WORKDIR /app

RUN addgroup --system flask && \
    adduser --system --ingroup flask flask

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY . .
RUN chown -R flask:flask /app
USER flask

ENV FLASK_APP=run.py
ENV FLASK_ENV=production

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

EXPOSE 5000
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:5000"]