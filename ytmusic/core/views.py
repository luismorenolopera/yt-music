from django.shortcuts import render
import youtube_dl
from django.conf import settings
from core.models import Song
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        return render(request,
                      'index.html',
                      context={'songs': songs})
    elif request.method == 'POST':
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': settings.BASE_DIR+'/media/music'+'/%(id)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.POST['url'])

        song = Song.objects.create(title=info['title'])
        song.file_data.name = '/music/{0}.mp3'.format(info['id'])
        song.save()
        return HttpResponseRedirect(reverse('index'))
