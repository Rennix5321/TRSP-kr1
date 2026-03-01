from fastapi import FastAPI
from models import Feedback

app = FastAPI()

feedbacks = []

@app.post("/feedback")
def create_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}