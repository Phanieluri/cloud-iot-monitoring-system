# Cloud IoT Monitoring System

A real-time cloud-based IoT monitoring system built using Python, MQTT, AWS EC2, Mosquitto, and Node-RED.

## Overview

This project demonstrates an end-to-end IoT data pipeline where environmental sensor data is simulated using Python and transmitted through MQTT to a cloud-hosted Mosquitto broker running on AWS EC2. Node-RED subscribes to the MQTT topic and visualizes the data through a real-time dashboard.

The system monitors:

* Temperature
* Humidity
* Pressure

Data is generated every 2 seconds and displayed instantly on the dashboard.

## System Architecture

Python Publisher → MQTT → Mosquitto Broker (AWS EC2) → Node-RED → Dashboard

## Features

* Real-time MQTT communication
* Cloud-hosted Mosquitto broker
* Multi-sensor data simulation
* Temperature monitoring
* Humidity monitoring
* Pressure monitoring
* Live gauges
* Live charts
* Real-time dashboard updates
* AWS EC2 deployment
* JSON-based data transmission

## Technologies Used

| Technology         | Purpose                       |
| ------------------ | ----------------------------- |
| Python             | Sensor data simulation        |
| MQTT               | Data communication protocol   |
| Mosquitto          | MQTT broker                   |
| AWS EC2            | Cloud hosting                 |
| Node-RED           | Data processing and dashboard |
| Node-RED Dashboard | Visualization                 |
| Ubuntu Linux       | Server operating system       |

## Project Workflow

1. Python generates random sensor values.
2. Data is converted into JSON format.
3. MQTT publishes the data to the Mosquitto broker.
4. Mosquitto receives and distributes the messages.
5. Node-RED subscribes to the MQTT topic.
6. JSON data is parsed and processed.
7. Dashboard widgets display live readings and charts.

## MQTT Topic

```text
sensor/multi
```

## Sample Payload

```json
{
  "temperature": 29,
  "humidity": 61,
  "pressure": 1008
}
```

## Dashboard Components

### Temperature Gauge

Displays current temperature values in real time.

### Humidity Gauge

Displays current humidity values in real time.

### Pressure Display

Displays current atmospheric pressure readings.

### Temperature History Chart

Visualizes temperature changes over time.

### Humidity History Chart

Visualizes humidity changes over time.

## Project Screenshots

### System Architecture

<img src="images/architecture.png" width="900">

### AWS EC2 Deployment

<img src="images/aws-ec2.png" width="900">

### Node-RED Flow

<img src="images/node-red-flow.png" width="900">

### Dashboard

<img src="images/dashboard.png" width="900">

## Setup Instructions

### AWS EC2

Create an Ubuntu EC2 instance and allow the following inbound ports:

| Port | Purpose  |
| ---- | -------- |
| 22   | SSH      |
| 1880 | Node-RED |
| 1883 | MQTT     |

### Install Mosquitto

```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients -y
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### Install Node-RED

```bash
sudo apt install nodejs npm -y
sudo npm install -g --unsafe-perm node-red
```

Start Node-RED:

```bash
node-red
```

Access:

```text
http://YOUR_PUBLIC_IP:1880
```

### Install Python MQTT Library

```bash
pip install paho-mqtt
```

### Run Publisher

```bash
python multi_sensor.py
```

## Repository Structure

```text
cloud-iot-monitoring-system/
│
├── README.md
├── multi_sensor.py
├── flow.json
│
├── images/
│   ├── architecture.png
│   ├── aws-ec2.png
│   ├── node-red-flow.png
│   └── dashboard.png
│
└── docs/
```

## Learning Outcomes

Through this project, I gained practical experience in:

* MQTT Publish/Subscribe Architecture
* Cloud Deployment using AWS EC2
* Mosquitto MQTT Broker Configuration
* Node-RED Flow Development
* JSON Data Processing
* Real-Time Dashboard Visualization
* IoT System Architecture Design

## Future Improvements

* ESP32 integration
* DHT11/DHT22 sensor integration
* Database storage
* Alert notifications
* HTTPS security
* MQTT authentication
* InfluxDB integration
* Grafana dashboards

## Author

Phaneendra

## License

This project is intended for educational and learning purposes.
