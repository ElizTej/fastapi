from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

# -------------------------------------------------
# class to validate the data coming from the frontend, once pased to the API
# the valdiation will be done by pydantic
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

# this class is the one that controls the filed that are returned when getting posts
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        # this class tells to pydantic model to convert into dict if it's not already a dict
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


# this is for the user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# -------------------------------------------------------------

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)