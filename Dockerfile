FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1

# Copy the requirements file to the container, and install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Create directory in the image for housing source code
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create a user for running applications only
RUN adduser -D user
USER user