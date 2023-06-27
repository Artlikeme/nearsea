from pydantic import BaseModel


class ApartmentList(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True


class ApartmentCreate(BaseModel):
    name: str
    description: str
    image: str
    address: str
    distance_to_sea: int
    type_id: int
    user_id: int
    tags_id: int
    apartment_rule_id: int
    square: int
    pledge: int
    max_num_of_guests: int
    storey: int

    # class Config:
    #     orm_mode = True
