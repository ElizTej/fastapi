from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hash the user password before saving it on the DB
def hash(password: str):
    return pwd_context.hash(password)

# to verify that user pass and the hashed pass are equal
def verify(plain_pass, hashed_pass):
    return pwd_context.verify(plain_pass, hashed_pass)
