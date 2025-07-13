# Dockerfile — Etsy Commander with FastAPI + Streamlit hybrid

FROM python:3.11-slim

# Avoid prompts
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --upgrade pip \
  && pip install streamlit fastapi uvicorn playwright \
  && playwright install --with-deps

# Expose Cloud Run default port
EXPOSE 8080

# Run main FastAPI + Streamlit hybrid server
CMD ["python", "main.py"]
