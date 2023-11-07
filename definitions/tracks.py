import strawberry
from definitions.users import User
from definitions.spotifyartist import SpotifyArtist
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
    def artists(self) -> List[SpotifyArtist]:
        artists = get_artists_from_track(self.track)
        new_lst = []
        for i in artists:
            art = SpotifyArtist(i)
            new_lst.append(art)
        return new_lst

    # analysis: object
    # features: object