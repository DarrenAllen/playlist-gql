import strawberry
from typing import List
from definitions.users import User
from definitions.tracks import Track
from services.tracks import read_tracks
from services.user import read_users

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
