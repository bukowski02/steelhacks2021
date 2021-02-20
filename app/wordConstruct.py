import ast
from utubedl import *
from dictionaryAPI import *

def flashcardCreate(word):

    f = open('transcripts.txt', 'r')
    _list = ast.literal_eval(f.read())
    f.close()

    loop = 0

    while loop == 0:
        for i in range(len(_list)):
            for e in range(len(_list[i])):
                if ' '+word in _list[i][e]['text']:
                    sentence = _list[i][e]['text']
                    code = _list[i][e]['code']
                    st = _list[i][e]['start']
                    dur = _list[i][e]['duration']
                    loop +=1

    mp3id = downloadAudio(code, word, st, dur)

    flashCard = {'sentence' : sentence,
                 'word': word,
                 'mp3id': mp3id
                }
    return flashCard

    
                
                
    
