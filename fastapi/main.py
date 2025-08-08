from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []
# get the root page whenever the server is started
@app.get("/")
def read_root():
        return {"Hello": "World"}

#we can create a new item using POST method
# command: curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=example_item'
@app.post("/items")
def create_item(item: str):
    items.append(item)
    return {"item": item, "message": "Item added successfully"}

#returns items in a list format upto the limit specified
# command: curl -X GET 'http://127.0.0.1:8000/items?limit=5'
#if no limit is specified, it defaults to 10 which is set in the function parameter
@app.get("/items")
def list_items(limit: int = 10):
     return items[0:limit]
        

# we can retrieve an item using GET method
# command: curl -X GET 'http://127.0.0.1:8000/items/0'
# where 0 is the index of the item in the items list
@app.get("/items/{item_id}")
def get_item(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:# Using exception handling to return a 404 error instead of a generic error message
        raise HTTPException(status_code=404, detail="Item not found")