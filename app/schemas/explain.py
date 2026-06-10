from pydantic import BaseModel

class ExplainRequest(BaseModel):
    vulnerability: str