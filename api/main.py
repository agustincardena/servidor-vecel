from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola desde FastAPI con Mangum en Vercel"}

# en vez de exponer la variable directamente
# exponemos una función que devuelve el Mangum handler
def handler(event, context):
    asgi_handler = Mangum(app)
    return asgi_handler(event, context)
