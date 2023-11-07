from sqlmodel import SQLModel, Field, JSON, Column

class Image(SQLModel):
    height: int
    width: int
    url: str

class SpotifyArtist(SQLModel):
    name: str
    totalFollowers: int
    popularity: int
    images: list[Image]
    
class Artists(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    uri: str
    artist: SpotifyArtist = Field(sa_column=Column(JSON))
    genres: list[str]
    