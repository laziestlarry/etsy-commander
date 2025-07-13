# Dockerfile — Etsy Commander Cloud Container

# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install streamlit playwright && playwright install chromium

# Expose port for Streamlit
EXPOSE 8501

# Start app
CMD ["streamlit", "run", "growth_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
