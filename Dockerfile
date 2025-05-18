FROM python:3.11-slim

RUN pip install paho-mqtt

COPY mqtt-proxy.py /mqtt-proxy.py
CMD ["python", "/mqtt-proxy.py"]
