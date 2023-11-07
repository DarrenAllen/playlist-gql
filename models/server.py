from sqlmodel import SQLModel, Field

class Servers(SQLModel, table=True):
    serverid: int = Field(default=None, primary_key=True)
    name: str
    