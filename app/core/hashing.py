from passlib.context import CryptContext
from app.config import cfg


pwd_context = CryptContext(schemes=[cfg.APP_SETTING.PASS_HASHING_ALGORITHM], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
