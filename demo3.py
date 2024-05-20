from fastapi import FastAPI
from enum import Enum

app = FastAPI()

food_items = {
    'indian' : ['samosa','Dosa'],
    'american' : ['Hot Dog','Apple Pie'] 
}

valid_cuisines = food_items.keys()

class AvaliableCuisines(str,Enum):
    indian = "indian"
    american = "american"

@app.get("/items/{cuisine}")

async def get_items(cuisine: AvaliableCuisines):
    return food_items.get(cuisine)