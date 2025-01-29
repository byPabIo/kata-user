
class InvalidJsonFormatException(Exception):
    def __init__(self, message:"No es un JSON valido."):
        self.message = message
        super().__init__(self.message)