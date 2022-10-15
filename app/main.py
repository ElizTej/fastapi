
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import posts, users, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# This is to be able to tell ORM to create the tables once code runs
# util until we have alembic, once alembic set then we dont need
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get('/')
def root():
    # http get method and the root path inside
    return {"message": "Welcome to my API!!!"}


# https://www.youtube.com/watch?v=0sOvCWFmrtA
# quede en 9:21 minutos
