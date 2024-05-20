from fastapi import FastAPI 

app = FastAPI()

food_items = {
    'south' : ["Dosa","Idly"],
    'north' : ["Poha","vadapav"]
}

@app.get("/items/{cuisine}")

async def get_items(cuisine):
    return food_items.get(cuisine)