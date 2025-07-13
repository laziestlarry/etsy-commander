FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --upgrade pip \
  && pip install streamlit fastapi uvicorn playwright \
  && playwright install --with-deps

# Fix Accept-CH and disable websocket compression
RUN mkdir -p ~/.streamlit && \
    echo "[server]\nheadless = true\nenableCORS = false\nenableXsrfProtection = false\nenableWebsocketCompression = false\n" > ~/.streamlit/config.toml

EXPOSE 8080

CMD ["python", "main.py"]
