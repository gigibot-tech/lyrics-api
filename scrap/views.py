from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from scrap.script import getlist
from scrap.script2 import getlyrics
from userdata.form import Song_all
from userdata.models import Song_table


def search(request):
    rb = getlist()
    return JsonResponse(json.dumps(
        {
        "key": getlist()
        }
    ,safe=False))

def results(request):

    result_url = request.GET.get('song_url', '')
    result_song = request.GET.get('song_name', '')
    result_artist = request.GET.get('song_artist', '')


#    try:
    song = Song_table()
    song.song_name = result_song
    song.song_artist = result_artist
    song.song_url = result_url
    song.user_email = request.user.username
    song.save()
#error

    get_lyrics_data = getlyrics(result_url)
    print(get_lyrics_data)


    return JsonResponse(json.dumps(
        {
        "lyrics": get_lyrics_data,
        "result_song": result_song,
        "result_artist": result_artist,
    }
    ,safe=False))