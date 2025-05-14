# 1. Base image with Python
FROM python:3.10-slim

# 2. Install ffmpeg for audio handling
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# 3. Set working directory
WORKDIR /app

# 4. Copy dependency list and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your application code
COPY . .

# 6. Default command: run your CLI
ENTRYPOINT ["python", "app.py"]
