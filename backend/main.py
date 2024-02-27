from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#APP Object
app = FastAPI()


origins = ["https://localhost:3000"]


# CORS middleware in this way, you're allowing requests from specified origins, including credentials, allowing all HTTP methods, and allowing all headers. Adjust these settings according to your specific requirements and security considerations.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return{"Ping":"Pong"}