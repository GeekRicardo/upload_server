from fastapi import FastAPI, File, UploadFile, HTTPException
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path
import shutil

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_location = f"{file.filename}"
        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)
    except Exception as e:
        raise HTTPException(status_code=400, detail="File upload failed")
    return {"info": f"file '{file.filename}' uploaded on server"}
