#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:40:05 2024

@author: raail
"""

#spotify_functions



def apiConnection():
    """ Establishes user connectivity to Spotify Web API """
    
    
    return


def get_playlist_tracks(username,playlist_id):
    """ Return a list user playlist and user tracks """
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks