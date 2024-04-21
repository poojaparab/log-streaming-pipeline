from fastapi import FastAPI, HTTPException
import httpx
from fluent import sender, event
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/produceEventsToPipeline")
async def send_logs_to_fluentd():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_json_logs/nginx_json_logs")
            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail="Failed to fetch logs")
            logs = response.text.splitlines()

            for log in logs:
                log_json = json.loads(log)
                sender.setup('app', host='fluentd', port=24224)
                event.Event('follow', log_json)
        return {"message": "Logs sent to Fluentd successfully", "status": "Success"}
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "Error: {e}", "status": "Failed"}

async def read_logs():
    try:
        asyncio.create_task(send_logs_to_fluentd())
        return {"message": "Logs fetching and sending initiated successfully"}
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail=str(e))

 

