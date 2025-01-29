from peewee import DoesNotExist

class UserNotFoundException(Exception):
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)

def get_user_or_raise(model, user_id):
    try:
        return model.get(model.id == user_id)
    except DoesNotExist:
        raise UserNotFoundException()
