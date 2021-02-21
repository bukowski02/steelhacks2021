import ast
from youtubeAPI import *
import pickle
import re
from collections import defaultdict

def flashcardCreate(word):

    f = open('transcripts.pkl', 'rb')
    transList = pickle.load(f)
    f.close()

    loop = 0
    while loop == 0:
        for video in transList:
            for wordseq in video:
                if ' '+word in wordseq['text']:
                    sentence = wordseq['text']
                    code     = wordseq['code']
                    st       = wordseq['start']
                    dur      = wordseq['duration']
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

    words = defaultdict(int)
    for video in transList:
        for sentence in video:
            es =  re.findall(r'[ ][a-zA-Z]+[ ]', sentence["text"]) + re.findall(r"[ ][a-zA-Z]+[\'][a-zA-Z]+[ ]", sentence["text"]);
            for word in es:
                words[word.lower()] += 1
    prev = sorted(words.items(),key = lambda x: -x[1])

    return [k[0] for k in prev]
                
                
    
