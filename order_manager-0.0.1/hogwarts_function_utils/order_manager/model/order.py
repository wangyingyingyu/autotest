from pydantic import BaseModel


class Order(BaseModel):
    id: int
    name: str
    count: int
