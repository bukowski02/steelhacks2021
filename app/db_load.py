from wordConstruct import *
from dictionaryAPI import *

def db_load():
    words = allWords()

    for word in words:
        for definition in getDef(word, "en", "gb"):
            addWordDB(word,str(definition)) #PLACEHOLDER FUNCTION NAME
        
        info = flashcardCreate(word)
        addFlashDB(word, -1, info["mp3id"],info["sentence"],0); #PLACEHOLDER FUNCTION NAME

db_load()