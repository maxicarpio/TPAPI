from pydantic import BaseModel

class Scholarship(BaseModel):
    id: int
    image: str
    name: str
    description: str
    price: int

class Programs(BaseModel):
    id: int
    image: str
    name: str
    description: str
    price: int

