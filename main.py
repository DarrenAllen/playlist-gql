from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from schema import Query

app = FastAPI()

schema = strawberry.Schema(query=Query)
app.mount("/graphql", GraphQL(schema, debug=True))