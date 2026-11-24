FROM python:3.11-slim
WORKDIR /app
COPY requests.py .
CMD ["python", "requests.py"]

# docker build -t heart-disease-requests:1 .
# docker run --rm -e API_URL=http://host.docker.internal:8000 heart-disease-requests:1
