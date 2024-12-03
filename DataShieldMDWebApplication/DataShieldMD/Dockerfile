# syntax=docker/dockerfile:1.4

FROM python:3.9-alpine AS builder

# Expose the application port
EXPOSE 8000

# Set the working directory
WORKDIR /DataShieldMD

# Install Python dependencies and OpenJDK
RUN apk update && apk add --no-cache \
    openjdk17 \
    openjdk17-jdk \
    build-base \
    bash \
    git

# Set JAVA_HOME and update PATH
ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk"
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Verify Java installation
RUN java -version

# Copy the requirements file and install Python dependencies
COPY requirements.txt /DataShieldMD
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . /DataShieldMD

# Entry point for the application
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
