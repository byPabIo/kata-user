class UserEntity:
    def __init__(self, username: str, password: str, person_id: str, activated: bool = True, date_created=None, date_modified=None):

        self.username = username
        self.password = password
        self.person_id = person_id
        self.activated = activated
        self.date_created = date_created
        self.date_modified = date_modified
