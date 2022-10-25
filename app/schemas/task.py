import uuid
from pydantic import BaseModel

class Task(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    isFinished: bool = False