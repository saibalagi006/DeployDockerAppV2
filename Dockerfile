# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variable for production
ENV FLASK_ENV=production

# Run the Flask app
CMD ["python", "main.py"]
