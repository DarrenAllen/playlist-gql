from fastapi import Depends, HTTPException, status
from models.tracks import Tracks
from models.user import Users
from models.artist import Artists
from sqlmodel import select
from database import get_session
from services.artist import flatten_artists
def read_tracks():
    db = next(get_session())
    tracks = db.exec(select(Tracks)).all()
    def get_added_by(track): 
        return track.track['track']['artists']
    first = get_added_by(tracks[0])
    print(first)
    return tracks

def get_added_by_from_track(track:object):
    uri = track['addedBy']['uri']
    db = next(get_session())
    user = db.exec(select(Users).where(Users.externalid == uri)).first()
    return user

def get_artists_from_track(track:object):
    artist_uri = track['track']['artists'][0]['uri']

    db = next(get_session())
    artist = db.exec(select(Artists).where(Artists.uri == artist_uri)).first()

    return [flatten_artists(artist)]
    

def old_get_artists_from_track(track:object):
    artists = track['track']['artists']
    
    def to_artist(artist: dict):
        class Artist:
            uri: str
            name: str
            externalURL: str
            
        newArt = Artist()
        newArt.name = artist['name']
        newArt.uri = artist['uri']
        newArt.externalURL = artist['externalURL']['spotify']
        return newArt
        
    return map(to_artist, artists)

