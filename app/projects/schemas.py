from pydantic import BaseModel

class ProjectBase(BaseModel):
    title: str
    description: Optional[str]

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectInDBBase(ProjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class Project(ProjectInDBBase):
    owner: User
    tasks: List[Task] = []

class ProjectInDB(ProjectInDBBase):
    pass
