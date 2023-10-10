from sqlmodel import SQLModel, Field

class Users(SQLModel, table=True):
    userid: int = Field(default=None, primary_key=True)
    username: str
    externalid: str
    nickname: str
    serverid: int
    discordid: str