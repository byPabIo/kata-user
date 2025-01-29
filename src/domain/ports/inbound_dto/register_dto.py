class RegisterDTO:
    def __init__(self, username: str, password: str, person_id: str):

        if not username or not password or not person_id:
            raise ValueError("Algunos campos están vacíos!")
        
        self.username = username
        self.password = password
        self.person_id = person_id
