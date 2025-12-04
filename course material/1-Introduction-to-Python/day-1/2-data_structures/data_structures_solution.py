# -*- coding: utf-8 -*-
"""
Solutions

"""

####Tuples####

#%% Tuple mit mehreren Werten
Texample = 1, 2
print(Texample)
#%% Tuple mit mehreren Werten
Texample2 = 1, 2, 3, 4, 5
print(Texample2)
#%% Tuple mit unterschiedlichen Datentypen
Texample3 = 1, 2, 3.0, "hey", True
print(Texample3)
#%% Indexabfrage
Texample[1]
#%% Index startet bei 0 (nicht 1)
Texample[0]
#%%
Texample2[4]
#%% welchen Index hat die Zahl 4
Texample2.index(4)
#%% welchen Index hat die Zahl 4 --> aber nur das erste Auftreten
Texample4 = 1,4,3,4,4,5
Texample4.index(4)
#%% mehrere Variablen gleichzeitig erzeugen
Texample5 = 3.0,4.0,12.0
dVarA, dVarB, dVarC = Texample5
#%% TypeError: 'tuple' object does not support item assignment
Texample6 = 4.0,8.0,16.0
Texample6[1] = 12.0

#%%
####Lists####

LNumbers = [1,2,3,4,5]
print(LNumbers)
#%% Liste mit mehreren Datentypen
LVarious = [1, 2, 3.0, "hey", True]
print(LVarious)
#%% Leere Listen
LEmpty = list()
LEmpty2 = []
print(LEmpty)
#%% Welcher Wert steht an Index 1
LVarious[1]
#%% Welchen Index hat das Element mit dem Wert 2
LVarious.index(2)
#%% Slicing --> Teilliste auswählen anhand des Index

LVarious[1:4]
#%%
LVariousPart = LVarious[1:4]
print(LVariousPart)
#%%
LSpotify = ["Charts","Neuheiten","Podcasts & Video Shows", "Entdecken", "Konzerte"]
#%% Listenelemente überschreiben
LSpotify[0] = "Aktuelle Charts"
#%% neues Listenelement hinten anhängen
LSpotify.append("Deine Songs")
#%% letztes Element wieder entfernen
LSpotify.pop()
print(LSpotify)
#%% Element an Index 3 entfernen
LSpotify.pop(3)
print(LSpotify)
#%% bestimmtes Element mithilfe des Wertes entfernen
LSpotify.remove("Neuheiten")
print(LSpotify)
#%% Element an bestimmtem Index einfügen
LSpotify.insert(1,"Neuheiten")
LSpotify.insert(3,"Entdecken")
print(LSpotify)
#%% Länge bzw. Größe der Liste
len(LSpotify)
#%% Zählen der Häufigkeit eines Elements
LSpotify.count("Neuheiten")
#%% Reihenfolge der Listenelemente umdrehen
LSpotify.reverse()
print(LSpotify)
#%%
LSpotify.reverse()
print(LSpotify)

#%% Strings funktionieren ähnlich wie Listen
sTestString = "Lists are awesome and so are Strings!"
sTestString[3]
sTestString[0:5]
len(sTestString)
#%%
####Sets####


SNumbers = {1,2,3,4,5,1}
print(SNumbers)
#%% Set mit verschiedenen Datentypen
SVarious = {1, 2, 3.0, "hey"}
print(SVarious)
#%% leeres Set
SEmpty = set()
print(SEmpty)
#%% prüfen ob ein Wert in Set enthalten ist
4 in SVarious
#%%
2 in SVarious
#%% Liste in Set umwandeln. Was fällt auf?
LtoSet = [1,2,3,5,2,4,12,523,123,21]
SfromList = set(LtoSet)
print(SfromList)
# {1, 2, 3, 4, 5, 523, 12, 21, 123}
#%% Liste aus Set erzeugen
LfromSet = list(SfromList)
print(LfromSet)

#%%
SNumbers = {1,2,3,4,5,1}
SVarious = {1, 2, 3.0, "hey"}

# unique in SNumbers
SNumbers
#%%
# in SNumbers, but not in SVarious
SNumbers - SVarious
#%%
# in SNumbers or in SVarious or both
SNumbers | SVarious
#%%
# in SNumbers and in SVarious
SNumbers & SVarious
#%%
# in SNumbers or in SVarious but not in both
SNumbers ^ SVarious
#%%
####Dictionaries####

DNumbers = {"One":1,"Two":2,"Three":3}
print(DNumbers)
#%% Zahlen als Keys und Values
DNumbers_nKeys = {1:1,2:2,3:3}
print(DNumbers_nKeys)
#%% Zahlen als Keys, Strings als Values
DNumbers_sVals = {1:"One",2:"Two",3:"Three"}
print(DNumbers_sVals)
#%% was sind die values die beim jeweiligen key hinterlegt sind
print(DNumbers_sVals[3])
print(DNumbers_sVals[1])
#%% Key neuen Value zuweisen
DNumbers_sVals[3] = "I made this."
print(DNumbers_sVals[3])
#%% prüfen, ob Key existiert, sonst Textausgabe
DNumbers_sVals.get(1,'This is the message, if no such key is in the dict.')
#%%
DNumbers_sVals.get(11,'This is the message, if no such key is in the dict.')
#%%
print(DNumbers_sVals[4])
#%% Strings als Keys, Dictionaries als Values
DSomeDicts = {"DNumbers":DNumbers, "DNumbers_nKeys": DNumbers_nKeys}
print(DSomeDicts)
#%%
DSomeDicts["DNumbers"]
DSomeDicts.get("DNumbers")
#%% Key eine Liste als Value zuweisen
DSomeDicts["DNumbers"] = [1,2,3]
print(DSomeDicts)
#%% neues Key Value Pair hinzufügen
DNumbers["SomeInt"] = 1337
print(DNumbers)
#%% entfernen anhand des Keys
DNumbers.pop("SomeInt")
print(DNumbers)

#%%
#### Exercises ####

# Create a variable of type list "LExercise" with the contents: "Anna", "Charles", "Peter", "Santa", "Eric"
LExercise = ["Anna", "Charles", "Peter", "Santa", "Eric"]
# Get the index of the element named "Santa"
LExercise.index("Santa")
# Get the element with the index 4
LExercise[4]
# Get the last element
LExercise[-1]
# Assign a string Variable with the contents of element with index 3, but only get the first three letters from the element!
SExerciseString = LExercise[3][:3]
####
# Create a variable of type dictionary "DExercise" with the key-value pairs: 4213-"Epic", 532-"Exclusive", 213-"Good", 5321-"Job"
DExercise = { 4213:"Epic", 532:"Exclusive", 213:"Good", 5321:"Job"}
# print the contents of the dictionary.
print(DExercise)
# Retrieve the list of keys.
DExercise.keys
# Retrieve the value for the key 532
DExercise[532]
####
# Create a list variable "LContainer" with the elements: [231,421,324,646],[21423,634,132],[123,765]
LContainer = [[231,421,324,646],[21423,634,132],[123,765]]
# Create a new variable iExampleMultiplication and assign the value of the multiplication between the 
# first element of the first list in LContainer and the third element of the second list in LContainer.
iExampleMultiplication = LContainer[0][0]*LContainer[1][2]