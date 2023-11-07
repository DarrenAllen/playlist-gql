import strawberry
from typing import List
from definitions.users import User
from definitions.tracks import Track
from definitions.spotifyartist import SpotifyArtist
from definitions.ideas import Idea
from services.tracks import read_tracks
from services.user import read_users
from services.artist import read_artists
from services.idea import read_ideas
# Define the root resolver
@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        users = read_users()
        return users
    
    @strawberry.field
    def tracks(self) -> List[Track]:
        tracks = read_tracks()
        return tracks
    
    @strawberry.field
    def spotifyartists(self) -> List[SpotifyArtist]:
        artists = read_artists()
        new_lst = []
        for i in artists:
            art = SpotifyArtist(i)
            new_lst.append(art)
        return new_lst
    
    @strawberry.field
    def ideas(self) -> List[Idea]:
        users = read_ideas()
        return users
    


# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def create_user(self, name: str) -> User:
#         return None

#     @strawberry.mutation
#     def update_user(self, id: int, name: str) -> User:
#         return None

#     @strawberry.mutation
#     def delete_user(self, id: int) -> User:
#         return None
