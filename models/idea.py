from sqlmodel import SQLModel, Field

class Ideas(SQLModel, table=True):
    ideaid: int = Field(default=None, primary_key=True)
    message: str
    