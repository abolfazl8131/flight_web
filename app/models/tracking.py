from pydantic import BaseModel,Field
from typing import List, Optional
from datetime import datetime,timezone



class InputTracking(BaseModel):
    Code:str
    

class Position(BaseModel):
    location:str = Field(default="default location",min_length=2 , max_length=200)
    datetime:datetime
    discription:Optional[str] = None


class OutPutTracking(BaseModel):
    fullname:str
    positions:List[Position]


    
