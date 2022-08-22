from typing import Any, Optional, Type
from uuid import uuid4
from datetime import datetime

from pydantic import BaseModel, validator, UUID4

from shortitpy.entities.app_error import AppError
from shortitpy.helpers.url_validation import is_valid_url
from shortitpy.helpers.gen_random import random_str


class ShortURL(BaseModel):
    id: Optional[UUID4]
    target_url: str
    access_key: Optional[str]
    access_url: Optional[str]
    created_at: Optional[datetime]

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        __pydantic_self__.id = data.get('id', uuid4())
        __pydantic_self__.access_key = data.get('access_key', random_str(12))
        __pydantic_self__.access_url = data.get('access_url', '')
        __pydantic_self__.target_url = data.get('target_url', __pydantic_self__.target_url)
        __pydantic_self__.created_at = data.get('created_at', datetime.now())

    @validator('target_url')
    def validate_target_url(cls, value):
        if not is_valid_url(value):
            raise AppError(msg='Invalid url!')

        return value
