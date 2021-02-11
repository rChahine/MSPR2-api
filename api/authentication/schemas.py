from pydantic import BaseModel, validators
import re


REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}$'


class NewUserSchema(BaseModel):
    identifiant: str
    password: str

    @validators('password')
    def validate_password(cls, v):
        if re.search(REGEX_PASSWORD, v):
            return v
        else:
            ValueError("password is not strong enough")
