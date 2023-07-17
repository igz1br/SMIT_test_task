from tortoise.models import Model
from tortoise import fields, Tortoise, run_async

class Insurance(Model):
    id = fields.IntField(pk=True)
    date = fields.TextField()
    type = fields.TextField()
    rate = fields.FloatField()

async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['model.model']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()

