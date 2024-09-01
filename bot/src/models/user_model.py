from pydantic import BaseModel

class SendedData(BaseModel):
    selectedDay: str
    selectedMonth: str
    selectedYear: str

class User_model(BaseModel):
    tg_id: int
    tg_name: str
    tg_lastname: str
    tg_username: str
    date_birth: SendedData

    def __str__(self):
        return f"{self.id} {self.tg_id} {self.date_birth}"

class BirthData(BaseModel):
    days_for_birth: int
    minutes_for_birth: int
    hours_for_birth: int

class User_birth_response(BaseModel):
    id :int
    tg_id: int
    tg_name: str
    tg_lastname: str
    tg_username: str
    birth_data : BirthData

    def __str__(self):
        return f"{self.id} {self.tg_id} {self.days_for_birth}"