import ast
from youtubeAPI import *
import pickle
import re

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

def allWords():

    f = open('transcripts.pkl', 'rb')
    transList = pickle.load(f)
    f.close()

    words = set()
    for video in transList:
        for sentence in video:
            es =  re.findall(r'[a-zA-Z]+', sentence["text"]) + re.findall(r"[a-zA-Z]+[\'][a-zA-Z]+", sentence["text"]);
            for word in es:
                words.add(word.lower())

    return list(words)
                
                
    
