from fastapi import FastAPI

app = FastAPI()
# Path: /items/{item_id}
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q":q}

# Path: /items/
@app.post("/items/")
async def create_item(item: Item):
    return item

# Path: /items/{item_id}
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# Path: /items/{item_id}
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}