from pydantic import BaseModel, EmailStr

class Media(BaseModel):
    media_url: str
    
class Technology(BaseModel):
    name:str

class ProjectBase(BaseModel):
    title: str

    # NOT REQUIRED
    github_link: str | None = None
    live_link: str | None = None

    # class Config():
    #     from_attributes =True

class CreateProject(ProjectBase):
    owner_id: str
    technologies: list[str]
    
class Project(ProjectBase):
    id: str 
    # relationships
    owner_id: str
    technologies: list[Technology] = []
    media: list[Media] = []

    class Config(): 
        from_attributes = True
        arbitrary_allowed_types = True

# USER SCHEMA
class UserBase(BaseModel):
    # REQUIRED
    email: EmailStr
    username: str
    first_name: str
    last_name: str

    # NOT REQUIRED
    bio: str | None = None
    title: str | None = None
    github: str | None = None
    twitter: str | None = None
    linkedIn: str | None = None 

    class Config():
        from_attributes =True

class CreateUser(UserBase):
    password: str
