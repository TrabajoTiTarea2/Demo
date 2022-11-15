from pydantic import BaseModel

class CharacterModel(BaseModel):
    name:str
    category:str
    list_price:float
