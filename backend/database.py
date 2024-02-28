#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

import motor.motor_asyncio  # motor.motor_asyncio: Async MongoDB driver for Python.
from model import Todo  # Todo: Importing the Todo model from the model.py module.

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/') # client: Connection to the MongoDB server at localhost:27017.
database = client.TodoList #database: Access to the database named TodoList.
collection = database.todo # collection: Access to the collection named todo within the TodoList database.


# fetch_one_todo(title): Asynchronously finds one document in the todo collection based on the provided title.
async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

# fetch_all_todos(): Asynchronously fetches all documents (todos) from the todo collection.
async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):  # create_todo(todo): Asynchronously inserts one document (todo) into the todo collection.
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc): # update_todo(title, desc): Asynchronously updates a document in the todo collection matching the provided title with the provided desc.
    await collection.update_one({"title": title}, {"$set": {"description": desc}})
    document = await collection.find_one({"title": title})
    return document

async def remove_todo(title): # remove_todo(title): Asynchronously deletes one document from the todo collection based on the provided title.
    await collection.delete_one({"title": title})
    return True