# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose port your app will run on
EXPOSE 8000

# Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "api.currency_converter.main:app", "--host", "0.0.0.0", "--port", "8000"]
