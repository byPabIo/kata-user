import uuid, peewee
from datetime import datetime

from peewee import Model, UUIDField, CharField, BooleanField, DateTimeField
from infrastructure.db.database import db

class UserModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    username = CharField(unique=True, null=False, max_length=200)
    password = CharField(null=False, max_length=255)
    activated = BooleanField(default=True)
    date_created = DateTimeField(default=datetime.utcnow)
    date_modified = DateTimeField(default=datetime.utcnow)

    class Meta:
        database = db
        table_name = 'users'

def set_username(self, username):
    """Convierte el nombre de usuario a minúsculas antes de guardarlo"""
    self.username = username.lower()
