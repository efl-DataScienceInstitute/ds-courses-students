# code for control structures slides


# %%
#6
# Define list of numbers from 1 to 10
LNumbers = [1,2,3,4,5,6,7,8,9,10]

# Alternative
LNumbers = list(range(1,11))


# %%
#10
iNumber = 5

if iNumber < 10:
    print('Number is less than 10')




# %%
#11
iNumber = 15
if iNumber < 10:
    print('Number is less than 10')
else:
    print('Number is greater or equal to 10')


age = 19
if not age < 18:
    print('Person is younger than 18')
elif age == 18:
    print('Person is 18')
elif age == 19:
    print('Person is 19')
else:
    print('Person is older than 19')



# %%
#13
iNumber = 5
if (iNumber + 5) < 10:
    print('Number plus 5 is smaller than 10')

if not (iNumber + 5) < 10:
    print('Number plus 5 is larger than 10')

if iNumber > 3 and iNumber < 10:
    print('Number is larger than 3 and smaller than 10')





# %%
#14
LNumbers = [1,2,3,4,5,6,7,8,9,10]
iNum = LNumbers[2]

if iNum % 2 == 0:
    print(iNum)







# %%
#15
    
#Exercise 1

#prints minimum of both numbers
iNum1 = 8
iNum2 = 5

if iNum1 <= iNum2:
	print(iNum1)
else:
	print(iNum2)
	
#prints grade based on received points
iPoints = 77

if iPoints >= 90:
	print('Grade 1')
elif iPoints >= 75:
	print('Grade 2')
elif iPoints >= 60:
	print('Grade 3')
elif iPoints >= 50:
	print('Grade 4')
else:
	print('Grade 5')



#16
#Exercise 2

(1+2) == 3

True != False

iNum = 4
(iNum != 0) and (20/iNum > 0) 


iHour = 12
(iHour < 9) or (iHour > 18) 




# %%
#20
count = 0
while (count < 3):
    count = count + 1
    print("Hello!") 







# %%
#21
LNumbers = [1,2,3,4,5,6,7,8,9,10]

for iNum in LNumbers:
    print(iNum)
    



# %%
#22
for i in list(range(1, 10, 2)):
    print(i)
    
 
# Iterating by index of sequences
LWords = ['Iterating', 'by', 'index', 'of', 'sequences']

for i in range(len(LWords)):
    print(LWords[i])
    
	
	
for element in LWords:
    print(element)




# %%
#23
for letter in 'science':  
    if letter == 'e' or letter == 'c': 
         continue
    print('Current Letter:', letter)



for letter in 'science':  
    if letter == 'e' or letter == 'c': 
         break
    print('Current Letter:', letter)



for letter in 'science': 
    pass
print('Last Letter :', letter)
    


# %%
#25
# Define list of numbers from 1 to 10
LNumbers = [1,2,3,4,5,6,7,8,9,10]

# Iterate over list
for iNum in LNumbers:
    # Check remainder of iNum
    if iNum % 2 == 0:
        # Print iNum if even
        print(iNum)
    
    
      
    
# %%
#26
    
#Exercise 3 
    
    
    
LNumbers = [5,23,37,49,50,46,30,46,70]

# 1. while loop
iCount = 0
iSizeofList = len(LNumbers)
i = 0

while i < iSizeofList:
	if LNumbers[i] > 30:
		iCount = iCount + 1
	i = i + 1

print(iCount)

# 2. for loop
iCount = 0

for n in LNumbers:
	if n > 30:
		iCount = iCount + 1
		
print(iCount)
    
    
    
