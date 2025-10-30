import secrets
from datetime import date, timezone, timedelta


class token_auth():
    def __init__(self):
        self.__token_HEX = None
        self.__token_Expiration = None

    @property
    def token_hex_getter(self):
        return self.__token_HEX
    
    @property
    def token_exp_getter(self):
        return self.__token_Expiration

    def token_setter(self):
        self.__token_HEX = secrets.token_hex(32)
        self.__token_Expiration = timezone.now() + timedelta(days=1)

