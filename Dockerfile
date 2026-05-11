FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install flask psutil prometheus_client

CMD ["python", "sensor_service.py"]