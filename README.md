# Log Streaming Pipeline Documentation

This repository contains a Docker Compose file and helper scripts to set up and manage a log streaming pipeline. The pipeline includes various services such as Fluentd, Kafka, Logstash, OpenSearch, Grafana, and others, aimed at collecting, processing, storing, and visualizing logs.

## Prerequisites

Before using the log streaming pipeline, ensure you have the following installed:

- Docker

## Getting Started

1. **Clone this repository:**

    ```bash
    git clone https://github.com/poojaparab/log-streaming-pipeline.git
    cd log-streaming-pipeline
    ```

2. **Initial configurations:**
   - Run ./bash-script-config.sh to make all the helper scripts executable. 

3. **Start the log streaming pipeline:**

    ```bash
    ./start-pipeline.sh
    ```
    
4. **Produce events to the pipeline:**

    ```bash
    ./produce-event.sh
    ```

5. **Monitor the pipeline:**

    ```bash
    ./monitor-pipeline.sh
    ```

6. **Stop the pipeline:**

    ```bash
    ./stop-pipeline.sh
    ```

7. **Check the status of pipeline components:**

    ```bash
    ./status-components.sh
    ```

## Helper Scripts

### 1. start-pipeline.sh

Starts the log streaming pipeline by executing `docker-compose up -d`.

### 2. stop-pipeline.sh

Stops the log streaming pipeline by executing `docker-compose down`.

### 3. produce-event.sh

Produces events to the pipeline by sending requests to the FastAPI web application hosted on `http://localhost:8000`.

### 4. monitor-pipeline.sh

Displays the Grafana dashboard link (`http://localhost:3000`) for monitoring the pipeline logs.

### 5. status-components.sh

Gives the status of all pipeline components by executing a Python script (`docker_status_app/app.py`).




## Contributors

- [Pooja Parab](https://github.com/poojaparab) - Creator

