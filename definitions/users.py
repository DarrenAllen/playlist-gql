import strawberry

@strawberry.type
class User:
    userid: int
    username: str
    externalid: str
    nickname: str
    serverid: int
    discordid: str