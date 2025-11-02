from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123xyz",
    city="Pune",
    postal_code="120210"
)

user = User(
    id=1,
    name="Vishwajeet",
    address=address
)

user_data = {
    "id": 1,
    "name": "Vishwajeet",
    "address": {
        "street": "321 something",
        "city": "Pune",
        "postal_code": "123321"
    }
}

user = User(**user_data)
print(user)