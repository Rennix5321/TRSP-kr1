from pydantic import BaseModel, Field, field_validator
import re

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator("message")
    def check_bad_words(cls, value):
        forbidden_words = ["кринж", "рофл", "вайб"]
        pattern = r"\b(" + "|".join(forbidden_words) + r")\w*\b"

        if re.search(pattern, value, re.IGNORECASE):
            raise ValueError("Использование недопустимых слов")

        return value