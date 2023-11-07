import strawberry

@strawberry.type
class Image:
    # This is poor form, I've killed type safety. I did it because of a circular dependancy when using the strawberry types in the service
    def __init__(self, dictionary):
         for k, v in dictionary.items():
            setattr(self, k, v)
    width: int
    height: int
    url: str