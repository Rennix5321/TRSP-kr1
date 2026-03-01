from fastapi import FastAPI
from models import User

app = FastAPI()

@app.post("/user")
def check_user(user: User):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }