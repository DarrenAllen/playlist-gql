import strawberry
from definitions.images import Image
@strawberry.type
class SpotifyArtist:
    # This is poor form, I've killed type safety. I did it because of a circular dependancy when using the strawberry types in the service
    def __init__(self, dictionary):
         for k, v in dictionary.items():
             if(k=='images'):
                new_lst = []
                for i in v:
                     image = Image(i)
                     new_lst.append(image)
                     
                setattr(self, k, new_lst)
             else:
                setattr(self, k, v)
    uri: str
    genres: list[str]
    popularity: int
    name: str
    totalFollowers: int
    images: list[Image]
    