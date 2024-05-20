from fastapi import FastAPI
app = FastAPI()

@app.get("/")

async def hello():
    return "Demo for FastAPI"


@app.get("/home/{name}")
async def home(name):
    return f"Hi This is {name}"

'''uvicorn demo:app --reload'''