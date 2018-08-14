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
        url = request.POST['url']
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': settings.BASE_DIR+'/media/music'+'/%(id)s.%(ext)s',
        }
        if len(url.split('list=')) > 1:
            try:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)

                    for video in info['entries']:
                        if not Song.objects.filter(file_data='/music/{0}.mp3'.format(video['id'])).exists():
                            song = Song.objects.create(title=video['title'],
                                                       thumbnail=video['thumbnail'])
                            song.file_data.name = '/music/{0}.mp3'.format(video['id'])
                            song.save()
            except Exception as e:
                print('error')
        else:
            if not Song.objects.filter(file_data='/music/{0}.mp3'.format(url.split('watch?v=')[1])).exists():
                try:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=True)
                        song = Song.objects.create(title=info['title'],
                                                   thumbnail=info['thumbnail'])
                    song.file_data.name = '/music/{0}.mp3'.format(info['id'])
                    song.save()
                except Exception as e:
                    print(e)
                    print('hello error')
        return HttpResponseRedirect(reverse('index'))
