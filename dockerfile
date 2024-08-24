FROM python:3.12-slim-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt

# Update distribution
RUN apt-get update \
    # Install all the pip modules
    && pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

CMD ["flask", "--debug", "run", "--port", "8080",  "--host=0.0.0.0"]