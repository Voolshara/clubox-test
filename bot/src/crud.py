from src.db.schemas import User
from src.models.user_model import User_model
from datetime import datetime

months = [
  "январь",
  "февраль",
  "март",
  "апрель",
  "май",
  "июнь",
  "июль",
  "август",
  "сентябрь",
  "октябрь",
  "ноябрь",
  "декабрь",
]

async def get_user_data(tg_id: int):
    selected_user = await User.filter(tg_id=tg_id)
    if len(selected_user) == 0:
        return None
    return selected_user[0]

async def add_user(user: User_model) -> User:
    date_birth = datetime(
        year=int(user.date_birth.selectedYear),
        month=months.index(user.date_birth.selectedMonth) + 1,
        day=int(user.date_birth.selectedDay),
    )
    user = User(
            tg_id=user.tg_id,
            tg_name=user.tg_name,
            tg_lastname=user.tg_lastname,
            tg_username=user.tg_username,
            date_birth=date_birth
        )
    await user.save()
    return user