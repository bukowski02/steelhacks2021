from __future__ import unicode_literals
import youtube_dl
import ffmpeg  
import os
import random

def downloadAudio(code, word, st, dur):
    ydl_opts = {
    'format': 'worstaudio/worst',
    'extractaudio' : True,
    'audioformat' : 'mp3',
    'outtmpl': word+'.mp3',
    'noplaylist' : True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v='+code])
        video = word+'.mp3'
        ID = random.randint(0,2**64-1)
        os.system('cmd /c "ffmpeg -ss '+str(st)+' -t '+str(dur)+' -i '+video+' video/'+str(ID)+'.mp3"')
        os.remove(video)
        return ID


    
