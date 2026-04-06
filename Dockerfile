FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Persistent log volume mount point
RUN mkdir -p /app/logs

ENV LOG_DIR=/app/logs
ENV HOST=0.0.0.0
ENV PORT=8338

EXPOSE ${PORT}

CMD ["sh", "-c", "uvicorn main:app --host ${HOST} --port ${PORT}"]
