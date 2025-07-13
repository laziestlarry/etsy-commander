FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set a proper HOME so Streamlit picks up configs
ENV HOME="/root"

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip \
  && pip install streamlit fastapi uvicorn playwright \
  && playwright install --with-deps

# Add stable Streamlit config
RUN mkdir -p $HOME/.streamlit && \
    echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
enableWebsocketCompression = false\n\
" > $HOME/.streamlit/config.toml

EXPOSE 8080

CMD ["python", "main.py"]
