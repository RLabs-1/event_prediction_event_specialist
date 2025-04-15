# Use the official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the main.py script into the container
COPY main.py .

# Define the command to run the script
CMD ["python", "main.py"]
