from datetime import datetime
from random import randint
from fastapi import Depends, FastAPI, HTTPException, Query, Request
from typing import Any

app = FastAPI(root_path="/api/v1")

data : Any = [
    {

    "id": 1,
    "name": "Summer Launch" ,
    "Campaign 1 date" : datetime.now(),
    "description": "Launching our new summer collection with a big sale!",
    "created_at" : datetime.now(),
    },
    {
        "id": 2,
    "name": "Winter Launch" ,
    "Campaign 2 date" : datetime.now(),
    "description": "Launching our new Winter collection with a big sale!",
    "created_at" : datetime.now(),
    }
]
@app.get("/")
async def read_root():
    return {"message": "Hello World!"}


@app.get("/campaigns")
async def read_campaigns():
    return {"campaigns": data}



@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    for campaign in data:
        if campaign.get("id") == id:
            return campaign
        
    raise HTTPException(status_code=404)


@app.post("/campaigns", status_code=201)
async def create_campaign(body: dict[str, Any]):

    new : Any = {
        "campaign_id": randint(100, 1000),
        "name": body.get("name"),
        "due_date": body.get("due_date"),
        "created_at": datetime.now()
    }
    
    data.append(new)
    return {"campaign": new}
