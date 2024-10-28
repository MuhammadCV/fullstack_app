# Use the official Python image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Expose the port the app runs on
EXPOSE 8000

# Start the Django server
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
