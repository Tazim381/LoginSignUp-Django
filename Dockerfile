# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variable to prevent Python from writing .pyc files to disk
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "loginSignUp.wsgi:application", "--bind", "0.0.0.0:8000"]
