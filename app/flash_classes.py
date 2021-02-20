import random
from collections import defaultdict

class Flashcard:

    def fromDict(dic): #factory that builds a flashcard from a preexisting dict
        out = Flashcard(dic["word"], ID=dic["id"], defns=dic["possDefns"]) #any word stored in a dictionary must have the first three fields.
        if "defn" in dic.keys(): #Unfilled fields are skipped rather than given None so that they can more easily be stored in JSON
            self.setDefinition("defn")
        if "exampleClipID" in dic.keys():
            self.setExample(dic["exampleClipID"],dic["examplePhrase"])
        return out
    
    def __init__(self, wrd, ID=None, defns=None):
        self.id   = random.randint(0,2**64-1)           #INT, unique ID
        if ID != None:
            self.id = ID
        
        self.word = wrd                                 #STR, word to be studied

        if defns == None:
            self.possDefns = findPossibleDefns(wrd)     #LST, possible definitions
        else:
            self.possDefns = defns
        self.defn = None                                #STR, definition selected by used based on context
        self.exampleClipID = None                       #INT, ID of sound clip
        self.examplePhrase = None                       #STR, Example phrase from sound clip

    def findPossibleDefns(word):
        return ["PLACEHOLDER"]
    
    def setExample(self, clipID, phrase):
        self.exampleClipID = clipID
        self.examplePhrase = phrase

    def setDefinition(self, indexOrStr):
        if isinstance(indexOrStr,int):
            self.defn = self.possDefns(indexOrStr)
        if isinstance(indexOrStr,str):
            self.defn = indexOrStr


    
    def toDict(self):
        out = {}
        for name,val in [("id",self.id),
                         ("word",self.word),
                         ("possDefns",self.possDefns),
                         ("defn",self.defn),
                         ("exampleClipID",self.exampleClipID),
                         ("examplePhrase",self.examplePhrase) ]:

            if val != None:
                out[name] = val
        return out
        

