# Use Alpine Python base image
FROM python:3.11-alpine

# Environment variables to prevent __pycache__ files and enable logging
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Install system dependencies required for psycopg2 and Django
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libpq-dev \
    libffi-dev \
    python3-dev \
    openssl-dev

# Copy only requirements file to leverage Docker cache
COPY requirements.txt /code/

# Install Python dependencies globally
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /code/
