from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status":"Raunak Ultra ERP AI API Live"}