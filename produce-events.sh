#!/bin/bash

WEBAPP_URL="http://localhost:8000"
API_ENDPOINT="/produceEventsToPipeline"

response=$(curl "${WEBAPP_URL}${API_ENDPOINT}")

echo $response