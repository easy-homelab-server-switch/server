FROM python:3.11-slim

RUN apt-get update && apt-get install -y dbus-x11 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app

RUN python3 -c "import paho.mqtt.client; print('Paho installed!')"

CMD ["python3", "-u", "main.py"]