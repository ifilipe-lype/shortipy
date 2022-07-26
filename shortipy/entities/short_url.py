from uuid import uuid4, UUID
from datetime import datetime

from pydantic import BaseModel, validator
from helpers.url_validation import is_valid_url

from entities.app_error import AppError
from helpers.gen_random import random_str

class ShortURL(BaseModel):
    id: UUID = uuid4()
    target_url: str
    access_key: str = random_str(12)
    created_at: datetime = datetime.now()

    @validator('target_url')
    def validate_target_url(cls, value):
        if not is_valid_url(value):
            raise AppError(msg='Invalid url!')
        
        return value

