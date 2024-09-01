from tortoise.models import Model
from tortoise import fields

class User(Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    id = fields.IntField(primary_key=True)
    tg_id = fields.IntField(unique=True, null=True)
    tg_name = fields.CharField(max_length=512)
    tg_lastname = fields.CharField(max_length=512)
    tg_username = fields.CharField(max_length=512)
    date_birth = fields.DateField()

    # Defining ``__str__`` is also optional, but gives you pretty
    # represent of model in debugger and interpreter
    def __str__(self):
        return f"{self.id} {self.tg_id} {self.date_birth}"
    