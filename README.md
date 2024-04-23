# Log Streaming Pipeline Documentation

This repository contains a Docker Compose file and helper scripts to set up and manage a log streaming pipeline. The pipeline includes various services such as Fastapi Web-app, Fluentd, Kafka, Logstash, OpenSearch, Grafana, and others, aimed at collecting, processing, storing, and visualizing logs.

## Prerequisites

Before using the log streaming pipeline, ensure you have the following installed:

- Docker
- Flask
- Python

## Architecture
![Image Alt Text](images\Architecture_diagram.png)

## Getting Started

1. **Clone this repository:**

    ```bash
    git clone https://github.com/poojaparab/log-streaming-pipeline.git
    cd log-streaming-pipeline
    ```

2. **Initial configurations:**
   - Run ./bash-script-config.sh to make all the helper scripts executable. 


## Helper Scripts Explained

### 1. start-pipeline.sh

    ```bash
    ./start-pipeline.sh
    ```

Starts the log streaming pipeline by executing `docker-compose up -d`.

### 2. stop-pipeline.sh

    ```bash
    ./stop-pipeline.sh
    ```

Stops the log streaming pipeline by executing `docker-compose down`.

### 3. produce-events.sh

    ```bash
    ./produce-events.sh
    ```

Produces events to the pipeline by sending requests to the FastAPI web application hosted on `http://localhost:8000`.

### 4. monitor-pipeline.sh

    ```bash
    ./monitor-pipeline.sh
    ```

Displays the Grafana dashboard link (`http://localhost:3000`) for monitoring the pipeline logs.

You can see the dashboard something like this:

![Image Alt Text](images\grafana.jpg)

### 5. get-pipeline-status.sh

Gives the status of all pipeline containers by executing a Python script (`docker_status_app/app.py`).
This application is running on: http://127.0.0.1:8111

status will  look like:
![Image Alt Text](images\docker-status.png)


## Contributors

- [Pooja Parab](https://github.com/poojaparab) - Creator

