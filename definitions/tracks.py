import strawberry
from definitions.users import User
from definitions.artists import Artist
from services.tracks import get_added_by_from_track, get_artists_from_track
from typing import List

@strawberry.type
class Track:
    trackid: int
    trackname: str
    playlistid: str
    uri: str 
    @strawberry.field
    def addedBy(self) -> User:
        user = get_added_by_from_track(self.track)
        return user
    
    @strawberry.field
    def artists(self) -> List[Artist]:
        user = get_artists_from_track(self.track)
        return user

    # analysis: object
    # features: object