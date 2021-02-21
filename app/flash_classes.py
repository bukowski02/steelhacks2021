import random
from collections import defaultdict
import random

class Flashcard:

    def fromDict(dic): #factory that builds a flashcard from a preexisting dict
        out = Flashcard(dic["word"], ID=dic["id"])
        out.setDefinition("defn")
        out.setExample(dic["exampleClipID"],dic["examplePhrase"])
        out.setLearned(dic["learned"])
        return out
    
    def __init__(self, wrd, ID=None):
        self.id   = random.randint(0,2**64-1)           #INT, unique ID
        if ID != None:
            self.id = ID
        
        self.word = wrd                                 #STR, word to be studied
        self.definition = None                          #INT, definition selected by used based on context, id in table
        self.exampleClipID = None                       #INT, ID of sound clip
        self.examplePhrase = None                       #STR, Example phrase from sound clip

        self.learned=False
    
    def setExample(self, clipID, phrase):
        self.exampleClipID = clipID
        self.examplePhrase = phrase

    def setDefinition(self, wordid):
        self.definition = wordid

    def setLearned(self,boolean):
        self.learned = boolean
    
    def toDict(self):
        out = {}
        for name,val in [("id",self.id),
                         ("word",self.word),
                         ("defn",self.defn),
                         ("exampleClipID",self.exampleClipID),
                         ("examplePhrase",self.examplePhrase),
                         ("learned",self.learned)]:
            out[name] = val
        return out
        
class FlashcardSet: #interface for flashcard database, as well as place for training functionality
    def __init__(self,ID):
        self.id = ID
        self.flashcardIDs = []
        self.loadFlashcardIDs()

        self.wordsToIDs = defaultdict(list)
        self.queue = []

        self.spacing = 15
                

    def loadFlashcardIDs(self):
        #TODO load them allllll [next is for later]
        #TODO load flash card IDs from self.id into self.flashcardIDs from database
        return

    def getFlashcard(self,cardid):
        
        if cardid not in self.flashcardIDs:
            raise ValueError("Card ID does not belong to this set.")
        
        data = {} #TODO drom database (this function will not work until then
            
        return Flashcard.fromDict(data)

    def weightedRandomWord(self):
        return random.choice(self.flashcardIDs); #TODO weight

    def initQueue(self):
        for k in range(self.spacing+2):
            self.queue.append(self.weightedRandomWord())

    def nextFlashcard(self):
        d = random.randint(-1,3)
        if d == -1:
            self.queue.append(self.weightedRandomWord())
        else:
            self.queue.append(self.queue[-(self.spacing+d)])
        return getFlashcard(self.queue.pop(0))

    
