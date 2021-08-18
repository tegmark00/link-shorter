# Dockerfile
# Pull base image
FROM python:3.9.5

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Add requirements
ADD /requirements.txt /requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app
