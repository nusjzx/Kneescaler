# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /mnt/ustorage/ce7490_P1
WORKDIR /app

# Copy the current directory contents into the container at /mnt/ustorage/ce7490_P1
COPY /app/ .

# Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME float_operation

# Run float_operation.py when the container launches
CMD ["python", "float_operation.py"]
