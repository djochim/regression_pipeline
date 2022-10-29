import uuid
from pydantic import BaseModel

class Task(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    name: str
    is_finished: bool = False