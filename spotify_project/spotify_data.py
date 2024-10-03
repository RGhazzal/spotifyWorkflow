#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:02:40 2024

@author: raail
"""
# main.py
import settings
import spotify_functions
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd




def get_playlist_tracks(username,playlist_id):
    """ """
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


# Set program scope global variables

SPOTIPY_CLIENT_ID = settings.CLIENTID
SPOTIPY_CLIENT_SECRET = settings.CLIENTSECRET
SPOTIFYSCOPE = 'user-library-read user-top-read user-read-private playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private'

SPOTIFY_REDIRECT_URL = "http://localhost:5000/callback"


client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                      client_secret=SPOTIPY_CLIENT_ID)


sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


all_tracks = spotify_functions.get_playlist_tracks('5catacombs', '2MRScQNSMsyQFrw0OYqH8o')
all_track_ids = []
for i in all_tracks:
    all_track_ids.append(i['track']['id'])