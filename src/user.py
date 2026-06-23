from dataclasses import dataclass
from hashlib import sha256
from typing import Optional

@dataclass
class User:
    id: int
    email: str
    password_hash: str
    google_id: Optional[str]

def create_user(email: str, password: str, google_id: Optional[str] = None) -> User:
    password_hash = sha256(password.encode()).hexdigest()
    return User(id=1, email=email, password_hash=password_hash, google_id=google_id)

def authenticate_user(email: str, password: str, users: list) -> Optional[User]:
    for user in users:
        if user.email == email and user.password_hash == sha256(password.encode()).hexdigest():
            return user
    return None
