from fastapi import FastAPI
from fastapi.responses import FileResponse
import requests
import os
import uvicorn
from dotenv import load_dotenv
from Services.Data_Fetcher import get_coin_data
from Services.report_collector import calculate_summary
from Services.report_generator import generate_pdf

app = FastAPI()

@app.get ("/report/{coin_id}")

def getData(coin_id):

    coin_data = get_coin_data(coin_id)
    calculate_result = calculate_summary(coin_data)
    generate_pdf(calculate_result)

    file_path = "Report.pdf"
    return FileResponse(file_path)