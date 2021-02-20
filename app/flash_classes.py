import random
from collections import defaultdict

class Flashcard:

    def fromDict(dic): #factory that builds a flashcard from a preexisting dict
        out = Flashcard(dic["word"], ID=dic["id"])
        self.setDefinition("defn")
        self.setExample(dic["exampleClipID"],dic["examplePhrase"])
        self.setLearned(dic["learned"])
        return out
    
    def __init__(self, wrd, ID=None):
        self.id   = random.randint(0,2**64-1)           #INT, unique ID
        if ID != None:
            self.id = ID
        
        self.word = wrd                                 #STR, word to be studied
        self.definition = None                          #STR, definition selected by used based on context
        self.exampleClipID = None                       #INT, ID of sound clip
        self.examplePhrase = None                       #STR, Example phrase from sound clip

        self.learned=False

    def findPossibleDefns(word):
        return ["PLACEHOLDER"]
    
    def setExample(self, clipID, phrase):
        self.exampleClipID = clipID
        self.examplePhrase = phrase

    def setDefinition(self, indexOrStr):
        if isinstance(indexOrStr,int):
            self.definition = self.possDefns(indexOrStr)
        if isinstance(indexOrStr,str):
            self.definition = indexOrStr

    def setLearned(boolean):
        self.learned = boolean
    
    def toDict(self):
        out = {}
        for name,val in [("id",self.id),
                         ("word",self.word),
                         ("defn",self.defn),
                         ("exampleClipID",self.exampleClipID),
                         ("examplePhrase",self.examplePhrase)
                         ("learned",self.learned]:
            out[name] = val
        return out
        
class FlashcardSet: #interface for flashcard database, as well as place for training functionality

    def __init__(ID):
        self.id = ID
        
        self.loadFlashcardIDs()
        self.loadedFlashcards = {}

        self.wordsToIDs = defaultdict(list)
        
        #TODO freq list
        

    def loadFlashcardIDs(self):
        #TODO load flash card IDs from self.id into self.flashcardIDs from database
        return

    def getFlashcard(self,cardid):
        
        if cardid not in self.flashcardIDs():
            raise ValueError("Card ID does not belong to this set.")
        
        if cardid not in self.loadedFlashcards.keys():
            data = {} #TODO drom database (this function will not work until then
            ou = Flashcard.fromDict(data)
            self.wordsToIDs[ou.word].append(ou.id)
            self.loadedFlashcards[cardid] = ou
            
        return self.loadedFlashcards[cardid]

    
