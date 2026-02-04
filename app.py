from fastapi import FastAPI

app = FastAPI()

@app.get("/hi/{name}")
def say_hi(name: str):
    return {"message": f"hi, {name}"}