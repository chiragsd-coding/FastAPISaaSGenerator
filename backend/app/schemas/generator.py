
from pydantic import BaseModel

class GenerateRequest(BaseModel):
    project_name:str
    db_type:str
    auth_type:str
