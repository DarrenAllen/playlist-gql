import strawberry

@strawberry.type
class Idea:
    ideaid: int
    message: str
   