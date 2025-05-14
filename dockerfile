# Use base Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt first for efficient caching
COPY requirements.txt /app/

# Install the dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code after installing dependencies
COPY . /app/

# Default command (can be overridden by docker-compose). ~Starts interactive terminal
CMD ["bash"]