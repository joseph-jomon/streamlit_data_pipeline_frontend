# syntax=docker/dockerfile:1

# Specify Python version as a build argument
ARG PYTHON_VERSION=3.11.4
FROM python:${PYTHON_VERSION}-slim as base

# Optimize Python behavior in Docker
ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1         

# Set the working directory at the root
WORKDIR /app

# Create a non-privileged user to run the application
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/home/appuser" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Create the home directory and give ownership to appuser
RUN mkdir -p /home/appuser && chown appuser:appuser /home/appuser

# Install dependencies from requirements.txt
# The --mount flag is used to cache pip packages during the build
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=/app/requirements.txt \
    python -m pip install --no-cache-dir -r /app/requirements.txt

# Copy the app directory to the container
COPY . /app

# Expose port for Streamlit (default port is 8501)
EXPOSE 8501

# Switch to non-privileged user
USER appuser

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
