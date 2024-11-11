FROM python:3.9-slim

WORKDIR /app

# Install MySQL client dependencies and curl
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev build-essential pkg-config curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD sleep 25 && uvicorn app.main:app --host 0.0.0.0 --port 8000
