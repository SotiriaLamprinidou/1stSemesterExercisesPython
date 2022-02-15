userInput = input("Give ASCII file name ")
# The file two_cities_ascii.txt is extremely large for this program's capacity. It is advised to use a smaller file in order to check it's functionality. 
# opening and reading file
f = open(userInput, "r") 
lines = f.read()
f.close()

#stores in a the variable only_alpha only the letters and the character space of the given file using the ASCII table
only_alpha = ""
for char in lines:
    if ord(char) >= 65 and ord(char) <= 90:
        only_alpha += char
    elif ord(char) >= 97 and ord(char) <= 122:
        only_alpha += char
    elif ord(char) == 32:
        only_alpha += char

#stores in a list every word 
list = only_alpha.split ()

#replaces with "" every 2 words if their sum is equal to 20 
for i in range(len(list)):
    count = len(list[i])
    for j in range(i+1,len(list)):
        count = count + len(list[j])
        if count == 20:
            list[i] = ""
            list[j] = ""
        count = len(list[i])

#searches for the largest word 
max = 0
for i in range(len(list)):
    if len(list[i]) > max:
        max = len(list[i])

#creates a table to store the number of words left 
A = [0]*(max+1)

for k in range(1,max+1):
    for m in range(len(list)):
        if len(list[m]) == k:
            A[k]= A[k]+1
A.pop(0)

#prints the results
c = 1
for i in A:
    print("There are", i, "words","with",c,"letters")
    c += 1