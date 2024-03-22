from pydantic import BaseModel

class City(BaseModel):
    cityName: str


class Transport(BaseModel):
    id: int
    name: str
    price_confort: str
    price_econ: str
    city: str
    duration: str
    seat: str
    bed: str
