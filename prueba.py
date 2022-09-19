from dataclasses import field
import os
import sys
import json
import requests
import cowsay
import re
import webbrowser
import spotipy
from cgi import print_exception
from helper import lookup,search_playlist, download_playlist, splink_to_ytlink, get_ids
from pytube import Search, YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 
from spotipy.oauth2 import SpotifyClientCredentials



save_path = 'C:/Users/POPOCHAN1990/Desktop'
link = "https://www.youtube.com/watch?v="
sp_song_link = "https://open.spotify.com/track/5CmIIBRVQWLX2uXAkuBlS8?si=23d548dc17bd45d6"

ids = get_ids()

try:
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=ids["client_id"], client_secret=ids["client_secret"]))
except:
    print("Spotify connection timeout. Possible causes: Internet slow, Ids wrong.")

s = search_playlist(spotify, "https://open.spotify.com/playlist/37i9dQZF1DXaPCIWxzZwR1?si=d5bd7accebc7463a")

download_playlist(spotify, s, save_path)