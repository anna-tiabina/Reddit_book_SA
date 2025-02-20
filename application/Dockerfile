# Use the official Python 3.11 image as the base image
FROM python:3.11

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory within the container
WORKDIR /application

# Copy the necessary files and directories into the container

COPY app_Reddit.py requirements.txt Dockerfile /application/
COPY test_pytest.py /application/
COPY test_unittest.py /application/
COPY static /application/static
COPY templates /application/templates

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn
CMD [ "python", "./app_Reddit.py" ]