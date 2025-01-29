import uuid
from peewee import Model, UUIDField, CharField, BooleanField, TimestampField
from infrastructure.db.database import db

class UserModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    username = CharField(unique=True, null=False, max_length=200)
    password = CharField(null=False, max_length=255)
    activated = BooleanField(default=True)
    date_created = TimestampField(constraints=['DEFAULT CURRENT_TIMESTAMP'])
    date_modified = TimestampField(constraints=['DEFAULT CURRENT_TIMESTAMP'])

    class Meta:
        database = db
        table_name = 'users'
