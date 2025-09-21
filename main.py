from mangum import Mangum
from app import app

# Mangum transforma la app ASGI (FastAPI) en un handler compatible con Lambda/Vercel
handler = Mangum(app)
