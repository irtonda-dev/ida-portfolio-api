from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

app = FastAPI()

class Visitor(BaseModel):
    name: str
    surname: str
    linkedin: Optional[HttpUrl] = None

#Function: Get
@app.get("/", summary="Root", description="Returns a welcome message confirming the API is running.")
def root():
    return {"message": "My name is Irton — Skills API is running"}    

#Function: pages/ContactMe > Submit button
@app.post("/visitors")
async def add_visitor(visitor: Visitor):
    log_visitor(visitor)
    # write to postgres later
    return {"status": "ok", "data": visitor}

#Logging actions

#Logs for a database
def log_visitor(visitor: Visitor):
    with open(LOG_DIR / "db_push.log", "a") as file:
        file.write(f"{datetime.now()}: {visitor.name} {visitor.surname} {visitor.linkedin}\n")

def log_action():
    #appended the log file with datetime + action
    with open(LOG_DIR / "api.log", "a") as file:
        file.write(f"{datetime.now()}: \n")
    return

def get_d_image():
    #Get the current image
    return 0

def trigger_gitpush():
    #this will push a git
    return 0


