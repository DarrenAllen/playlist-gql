from fastapi import Depends, HTTPException, status
from models.artist import Artists
from sqlmodel import Session, select
from database import get_session

def read_artists():
    db = next(get_session())
    artists = db.exec(select(Artists)).all()
    
    def flatten_artists(artist:Artists):
        newArtist = {'id': artist.id, 'name':artist.artist['name'],'uri':artist.uri, 'genres':artist.genres,'popularity': artist.artist['popularity'], 'totalFollowers':artist.artist['totalFollowers'], 'images':artist.artist["images"]}
        return newArtist
    
    newArtists = map(flatten_artists, artists)
    my_list = list(newArtists)
    return my_list

