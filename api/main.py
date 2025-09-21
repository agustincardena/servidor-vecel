from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI en Vercel!"}

handler = Mangum(app)
