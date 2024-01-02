# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

COPY . /app
# Copy the requirements file into the container at /app
COPY . requirements.txt /app/

RUN pip install --upgrade pip

# Install ny needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /ap

EXPOSE 8000

# Run the Django app
CMD ["python", "manage.py ", "runserver", "0.0.0.0:8000"]
