# Log Streaming Pipeline 

This repository contains a Docker Compose file and helper scripts to set up and manage a log streaming pipeline. The pipeline includes various services such as Fastapi Web-app, Fluentd, Kafka, Logstash, OpenSearch, Grafana, and others, aimed at collecting, processing, storing, and visualizing logs.

## Prerequisites

Before using the log streaming pipeline, ensure you have the following installed:

- Docker
- Flask
- Python

## Architecture
![Image Alt Text](https://github.com/poojaparab/log-streaming-pipeline/blob/main/images/Architecture_diagram.png)

## Getting Started

1. **Clone this repository:**

    ```bash
    git clone https://github.com/poojaparab/log-streaming-pipeline.git
    cd log-streaming-pipeline
    ```

2. **Initial configurations:**
   - Run ./bash-script-config.sh to make all the helper scripts executable. 


## Helper Scripts Explained

### a. Start the data pipeline.

    ./start-pipeline.sh

Starts the log streaming pipeline by executing `docker-compose up -d`.

### b. Stop the data pipeline.

    ./stop-pipeline.sh

Stops the log streaming pipeline by executing `docker-compose down`.

### c. Produce the events to the data pipeline.

    ./produce-events.sh

Produces events to the pipeline by sending requests to the FastAPI web application hosted on `http://localhost:8000`.

### d. Monitor the data pipeline.

    ./monitor-pipeline.sh

Displays the Grafana dashboard link (`http://localhost:3000`) for monitoring the pipeline logs.

You can see the dashboard something like this:

![Image Alt Text](https://github.com/poojaparab/log-streaming-pipeline/blob/main/images/grafana.jpg)

### e. Give the status of all of the components of the data pipeline.

Gives the status of all pipeline containers by executing a Python script (`docker_status_app/app.py`).
This application is running on: http://127.0.0.1:8111

![Image Alt Text](https://github.com/poojaparab/log-streaming-pipeline/blob/main/images/docker-status.png)

## Final Product: OpenSearch Dashboard

Once the log streaming pipeline is up and running, you can visualize the logs using the OpenSearch dashboard. The dashboard provides comprehensive visualization and analysis capabilities for your log data.

![OpenSearch Dashboard](https://github.com/poojaparab/log-streaming-pipeline/blob/main/images/On_demand_report_2024-04-23T00_17_44.501Z_e7f85d60-0106-11ef-8d00-9dbb035a2112.png)

## Contributors

- [Pooja Parab](https://github.com/poojaparab) - Creator

