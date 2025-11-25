import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home ():
    return {"message": "Welcome to Randomizer API"}


@app.get ("/random/{max_value}")
async def get_random_number (max_value:int):
    return{
        "max":max_value,
      "random_number":random.randint(1,max_value)
    }