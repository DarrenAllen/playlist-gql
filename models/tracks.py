from sqlmodel import SQLModel, Field, JSON, Column
from typing import Dict, Any

class Artist(SQLModel):
    id: int
    name: str

class AddedBy(SQLModel):
    uri: str
    name: str

class SpotifyTrack(SQLModel):
    artists: list[Artist]

class Track(SQLModel):
    addedBy: AddedBy
    track: SpotifyTrack 
    
    
class Tracks(SQLModel, table=True):
    trackid: int = Field(default=None, primary_key=True)
    trackname: str
    playlistid: str
    uri: str 
    # track: dict = Field(sa_column=Column(JSON), default={'all': 'true'})
    track: Track = Field(sa_column=Column(JSON))
    
    class Config:
        arbitrary_types_allowed = True 
   