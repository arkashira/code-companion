from dataclasses import dataclass
from typing import Optional

@dataclass
class Project:
    id: int
    name: str
    runtime: str
    user_id: int

def create_project(name: str, runtime: str, user_id: int) -> Project:
    return Project(id=1, name=name, runtime=runtime, user_id=user_id)
