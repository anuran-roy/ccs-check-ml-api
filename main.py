from fastapi import FastAPI
from routes import check

app = FastAPI()
app.include_router(check.router)

@app.get("/")
async def hello():
    return {"message": "Hello"}



