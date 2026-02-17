# Base image
FROM python:3.11-slim

# Install system dependencies
# Hugo (extended version for SCSS support if needed), Git, Curl for Firebase CLI
RUN apt-get update && apt-get install -y \
    curl \
    git \
    wget \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Hugo Extended
ENV HUGO_VERSION=0.121.1
RUN wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz \
    && tar -zxvf hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz \
    && mv hugo /usr/local/bin/ \
    && rm hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz

# Install Firebase CLI
RUN curl -sL https://firebase.tools | bash

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Initialize Hugo site if not exists (or assume it exists)
# For this setup, we assume 'blog' directory exists with Hugo structure

# Check if blog directory exists, if not init (safety check)
# RUN if [ ! -d "blog" ]; then hugo new site blog; fi

# Script to run the automation
COPY scripts/entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
