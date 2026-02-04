from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int

@app.post("/greet")
def greet_person(person: Person):
    return {"message": f"Hi {person.name}, you are {person.age} years old!"}