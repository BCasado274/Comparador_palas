from pydantic import BaseModel

class Pala(BaseModel):
    id: int
    nombre: str
    precio: float
    url: str
    imagen: str
    tienda: str
