# Use a lightweight official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code and the test script into the container
# The period '.' refers to the current directory on the host
COPY calculator.py .
COPY test_calculator.py .

# Command to run the application when the container starts
# This is the entry point for the running container
CMD ["python", "calculator.py"]