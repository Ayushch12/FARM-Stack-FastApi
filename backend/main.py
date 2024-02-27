from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

#APP Object
app = FastAPI()

from database import(
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
     update_todo,
     remove_todo

)

origins = ["https://localhost:3000"]

# CORS middleware in this way, you're allowing requests from specified origins, including credentials, allowing all HTTP methods, and allowing all headers. Adjust these settings according to your specific requirements and security considerations.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#GET
@app.get("/")
def read_root():
    return{"Ping":"Pong"}

@app.get("/api/todo")
async def get_todo():
    return 1

@app.get("/api/todo{id}")
async def get_todo_by_id(id):
    return 1

#POST
@app.post("/api/todo")
async def post_todo(todo):
    return 1

#DELETE
@app.delete("/api/todo{id}")
async def delete_todo(id):
    return 1

#UPDATE
@app.put("/api/todo{id}")
async def put_todo(id, data):
    return 1


