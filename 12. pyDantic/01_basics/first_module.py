# import BaseModel
from pydantic import BaseModel

class User(BaseModel):
    # Type Annotation
    id: int
    name: str
    is_active: bool

input_data = {'id': "101a", 'name': "Chaicode", 'is_active': True}

# Model init (Always unpack the dictionary)
# Automatic validation
user = User(**input_data)
print(user)