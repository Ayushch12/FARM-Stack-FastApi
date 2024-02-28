# With database connection --------------------------------------

# FastAPI: Web framework for building APIs.
from fastapi import FastAPI, HTTPException  # HTTPException: An exception class for generating HTTP exception information.

from model import Todo # Todo: Importing the Todo model from the model.py module.

from database import ( # Functions from database.py for CRUD operations.
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware  # Configures Cross-Origin Resource Sharing (CORS) middleware to allow requests from http://localhost:3000.
app = FastAPI()  # app: Instance of FastAPI for defining API routes.

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GET --------------
@app.get("/")   # @app.get("/"): Root endpoint returning a simple "Hello World" message.
async def read_root():
    return {"Hello": "World"}

# GET --------------
@app.get("/api/todo") # app.get("/api/todo"): Endpoint to fetch all todos.
async def get_todo():
    response = await fetch_all_todos()
    return response

# GET --------------
@app.get("/api/todo/{title}", response_model=Todo) # @app.get("/api/todo/{title}"): Endpoint to fetch a todo by its title.
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

# POST --------------
@app.post("/api/todo/", response_model=Todo) # @app.post("/api/todo/"): Endpoint to create a new todo.
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

# UPDATE --------------
@app.put("/api/todo/{title}/", response_model=Todo) # @app.put("/api/todo/{title}/"): Endpoint to update a todo by its title.
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

# DELETE --------------
@app.delete("/api/todo/{title}") # @app.delete("/api/todo/{title}"): Endpoint to delete a todo by its title.
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")




# # With out database connection --------------------------------------


# from fastapi import FastAPI, HTTPException
# from model import Todo

# app = FastAPI()

# # CORS Middleware configuration
# from fastapi.middleware.cors import CORSMiddleware

# origins = [
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Sample root endpoint
# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# # Sample API endpoints for Todo CRUD operations
# @app.get("/api/todo")
# async def get_todo():
#     # This could be replaced with database operations if added later
#     return [{"title": "Sample Todo", "description": "This is a sample todo"}]

# @app.get("/api/todo/{title}", response_model=Todo)
# async def get_todo_by_title(title: str):
#     # This could be replaced with database operations if added later
#     if title == "Sample Todo":
#         return Todo(title=title, description="This is a sample todo")
#     else:
#         raise HTTPException(status_code=404, detail="Todo not found")

# @app.post("/api/todo/", response_model=Todo)
# async def post_todo(todo: Todo):
#     # This could be replaced with database operations if added later
#     return todo

# @app.put("/api/todo/{title}/", response_model=Todo)
# async def put_todo(title: str, desc: str):
#     # This could be replaced with database operations if added later
#     return {"title": title, "description": desc}

# @app.delete("/api/todo/{title}")
# async def delete_todo(title: str):
#     # This could be replaced with database operations if added later
#     return {"message": f"Todo '{title}' deleted successfully"}
