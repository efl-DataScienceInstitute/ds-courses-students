# -*- coding: utf-8 -*-
"""
###############################################################################
#																										
# Do not forget: This Notebook is split into "Code Cells" with the command #%%.							
# You can run these cells with the keyboard combo: Strg/Ctrl + Enter	 								
# You can also use #%% to create a new separate cell, if you need it.									
#
###############################################################################
"""

####Tuples####

Texample = 1, 2
print(Texample)
#%%
Texample2 = 1, 2, 3, 4, 5
print(Texample2)
#%%
Texample3 = 1, 2, 3.0, "hey", True
print(Texample3)
#%%
print(Texample[1])
#%%
print(Texample[0])
#%%
print(Texample2[4])
#%%
print(Texample2.index(4))
#%%
Texample4 = 1,4,3,4,4,5
print(Texample4.index(4))
#%%
Texample5 = 3.0,4.0,12.0
dVarA, dVarB, dVarC = Texample5
print(dVarA)
#%%
Texample6 = 4.0,8.0,16.0
Texample6[1] = 12.0

Texample6.insert(2, 2)
#%%
LnewList = []
LsecondList = list()
LNumbers = [1, 2, 3, 4, 5]
print(LNumbers)
#%%
LVarious = [1, 2, 3.0, "hey", True]
print(LVarious)
#%%
LEmpty = list()
LEmptyOther = []
print(LEmpty)
#%%
print(LVarious[3])
#%%
print(LVarious.index(2)) 
#%%

print(LVarious[0:3])
#%%
LVariousPart = LVarious[0:3]
print(LVariousPart)

LNames = ['Anna', 'Peter']
LAges = [23, 25]
LPeople = [LNames, LAges]
LPeople[0][1]
#%%
LSpotify = ["Charts","Neuheiten","Podcasts & Video Shows", "Entdecken", "Konzerte"]

LSpotify[0] = "Aktuelle Charts"
print(LSpotify)
#%%
LSpotify.append("Favoriten")
#%%
LSpotify.pop()
print(LSpotify)
#%%
LSpotify.pop(3)
print(LSpotify)
#%%
LSpotify.remove("Neuheiten")
print(LSpotify)

LSpotify.remove("Lustige Lieder")
#%%
LSpotify.insert(1, "Neuheiten")
#%%
LSpotify.insert(3, "Entdecken")
print(LSpotify)
#%%
print(len(LSpotify))
#%%
print(LSpotify.count("Neuheiten"))
print(LSpotify.count("Lustige Lieder"))
#%%
LSpotify.reverse()
print(LSpotify)
#%%
LSpotify.reverse()
print(LSpotify)
#%%
sTestString = "Lists are awesome and so are Strings!"
#%%
print(sTestString[3])
#%%
print(sTestString[0:5]) # Play a little! Change the first and the second value.
#%%
len(sTestString)
#%%
####Sets####


SNumbers = {1,2,3,4,5,1}
print(SNumbers)
#%%
SVarious = {1, 2, 3.0, "hey"}
print(SVarious)
#%%
SEmpty = set()
print(SEmpty)
#%%

print(4 in SVarious)
#%%
print(2 in SVarious)
#%%
LtoSet = [1,2,3,5,2,4,12,523,123,21]
SfromList = set(LtoSet)
print(SfromList)
#%%
LfromSet = list(SfromList)
print(LfromSet)
#%%
SNumbers = {1,2,3,4,5,1}
SVarious = {1, 2, 3.0, "hey"}

# unique in SNumbers
print(SNumbers)
#%%
# in SNumbers, but not in SVarious
print(SNumbers - SVarious)
#%%
# in SNumbers or in SVarious or both
print(SNumbers | SVarious)
print(SVarious | SNumbers)
#%%
# in SNumbers and in SVarious
print(SNumbers & SVarious)
print(SVarious & SNumbers)
#%%
# in SNumbers or in SVarious but not in both
print(SNumbers ^ SVarious)
#%%
####Dictionaries####

DNumbers = {"One":1,"Two":2,"Three":3}
print(DNumbers)
#%%
DNumbers_nKeys = {1:1,2:2,3:3}
print(DNumbers_nKeys)
#%%
DNumbers_sVals = {1:"One",2:"Two",3:"Three"}
print(DNumbers_sVals)
#%%
print(DNumbers_sVals[3])
print(DNumbers_sVals[1])
#%%
DNumbers_sVals[3] = "I made this"
print(DNumbers_sVals[3])
#%%
print(DNumbers_sVals.get(1, "Show this if not in dict"))
#%%
print(DNumbers_sVals.get(5, "Show this if not in dict"))
#%%
print(DNumbers_sVals[5])
#%%
DSomeDicts = {"DNumbers":DNumbers, "DNumbers_nKeys": DNumbers_nKeys}
print(DSomeDicts)
#%%
print(DSomeDicts["DNumbers"])
print(DSomeDicts.get("DNumbers"))
#%%
DSomeDicts["SomeInt"] = 1337
print(DSomeDicts)
#%%
DNumbers["DNumbers"] = [1, 2, 3]
print(DNumbers)
#%%
DNumbers.pop("SomeInt")


DSomeDicts.pop("SomeInt")
print(DSomeDicts)
#%%

###################
#### Exercises ####
###################

#########################################################################################################
#																										#
# Do not forget: Insert #%% to create a new separate cell, which you can run with Strg/Ctrl + Enter		#
#																										#
#########################################################################################################

#%%

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