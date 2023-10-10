import strawberry

@strawberry.type
class Artist:
    uri: str
    name: str
    externalURL: str