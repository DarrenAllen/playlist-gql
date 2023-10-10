from sqlmodel import Session, SQLModel, create_engine

from config import settings

connect_args = {}
engine = create_engine(settings.DATABASE_URI, echo=False, connect_args=connect_args)


def get_session():
    with Session(engine) as session:
        yield session