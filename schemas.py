from pydantic import BaseModel

class Details(BaseModel):
    lastname:str
    firstname:str
    email:str

class ShowDetails(Details):
    class Config():
        orm_mode=True