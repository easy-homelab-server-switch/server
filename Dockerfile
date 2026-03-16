FROM python:3.11-slim

COPY requirements.txt .

RUN apt-get update && apt-get install -y dbus-x11 && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

RUN python3 -c "import paho.mqtt.client; print('Paho installed!')"

CMD ["python3", "-u", "main.py"]