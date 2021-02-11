from pydantic import BaseModel, validator
import re

from fastapi import HTTPException


class NewUserSchema(BaseModel):
    identifiant: str
    password: str

    @validator('password')
    def validate_password(cls, v):
        REGEX_PASSWORD = r'(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,}'
        if re.search(REGEX_PASSWORD, v) is not None:
            return v
        else:
            raise HTTPException(status_code=422, detail="Password not strong enough")
