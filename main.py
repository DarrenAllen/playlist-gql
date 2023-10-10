from fastapi import FastAPI
from typing import List
import strawberry
from strawberry.asgi import GraphQL
from public.user import read_users
from public.tracks import read_tracks, get_added_by_from_track, get_artists_from_track
app = FastAPI()


@strawberry.type
class User:
    userid: int
    username: str
    externalid: str
    nickname: str
    serverid: int
    discordid: str
    
@strawberry.type
class Artist:
    uri: str
    name: str
    externalURL: str
    
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
    
    # @strawberry.field
    # def user(self, id: int) -> User:
    #     return None


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


def get_next_id():
        return None


schema = strawberry.Schema(query=Query)
app.mount("/graphql", GraphQL(schema, debug=True))