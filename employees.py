from pydantic import BaseModel

class Employee(BaseModel):
    YearsExperience: float
    jobTitle: str