from database import Base
from sqlalchemy import Column, String, Integer, UUID, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from uuid import uuid4


def getUUID():
    return str(uuid4())

Project_Technology = Table('Project_Technology', Base.metadata,
    Column('project_id', String, ForeignKey('Project.id')),
    Column('technology_id', String, ForeignKey('Technology.id'))
)

class Technology(Base):

    __tablename__ = "Technology"
    id = Column(String, default=getUUID, primary_key=True)
    name = Column(String, unique=True, index=True)
    projects = relationship("Project", secondary=Project_Technology, back_populates="technologies")

    def __repr__(self):
        return f'<Technology "{self.id}": {self.name} >'
    

class Project(Base):

    __tablename__ = "Project"
    id = Column(String, primary_key=True, default=getUUID, index=True)
    title = Column(String, nullable=False, unique=True)
    github_link = Column(String)
    live_link = Column(String)

    owner_id = Column(String, ForeignKey("User.id"))
    owner = relationship("User", back_populates="projects")
    technologies = relationship("Technology", secondary=Project_Technology, back_populates="projects")

    def __repr__(self):
        return f'<Project "{self.id}: {self.title}">'




class User(Base):
    __tablename__ = "User"
    
    id = Column(String, nullable=False, primary_key=True, default=getUUID)
    username = Column(String, nullable=False, unique=True, index=True)
    email = Column(String, index=True)
    full_name = Column(String, nullable=False)
    bio = Column(String)
    title = Column(String)
    github_link = Column(String)
    twitter_link = Column(String)
    linkedIn_link = Column(String)

    # relationship
    projects = relationship("Project", back_populates="owner")

    def __repr__(self):
        return f'<User "{self.id}: {self.full_name}">'

