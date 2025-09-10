from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI running in Docker!"}

@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"hello, {name}!"}
