import ast
from youtubeAPI import *
import pickle

def flashcardCreate(word):

    f = open('transcripts.pkl', 'rb')
    transList = pickle.load(f)
    f.close()

    loop = 0
    while loop == 0:
        for video in transList:
            for sentence in video:
                if ' '+word in sentence['text']:
                    sentence = sentence['text']
                    code     = sentence['code']
                    st       = sentence['start']
                    dur      = sentence['duration']
                    loop +=1

    mp3id = downloadAudio(code, word, st, dur)

    flashCard = {
                 'sentence' : sentence,
                 'word': word,
                 'mp3id': mp3id
                }

    return flashCard

    
                
                
    
