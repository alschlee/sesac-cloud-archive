from typing import Optional
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, Session, create_engine

class Settings(BaseSettings):
    database_url: Optional[str] = None
    SECRET_KEY: Optional[str]  = None

    class Config:
        env_file = ".env"

settings = Settings()

#database_file = "planner.db"
#database_connection_string = f"sqlite:///{database_file}"
#connect_args = {"check_same_thread": False}
#engine_url = create_engine(database_connection_string, echo = True, connect_args=connect_args)

#database_url = os.getenv("DATABASE_URL", "default_connection_string")
engine_url = create_engine(settings.database_url, echo=True)

def conn():
    SQLModel.metadata.create_all(engine_url)

def getSession():
    with Session(engine_url) as session:
        yield session