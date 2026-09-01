from fastapi import FastAPI
import requests
import os
import uvicorn
from dotenv import load_dotenv

app = FastAPI()

@app.get('/')

def getData():

    return getData