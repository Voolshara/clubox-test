from datetime import date
from pydantic import BaseModel

class User_model(BaseModel):
    id :int
    tg_id: int
    tg_name: str
    tg_lastname: str
    tg_username: str
    date_birth: date

    def __str__(self):
        return f"{self.id} {self.tg_id} {self.date_birth}"


class User_birth_response(BaseModel):
    id :int
    tg_id: int
    tg_name: str
    tg_lastname: str
    tg_username: str
    days_for_birth: int

    def __str__(self):
        return f"{self.id} {self.tg_id} {self.days_for_birth}"