from urllib.request import Request, urlopen


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})

data = urlopen(req).read()

#storing data as a string in mydata
mydata = str(data)

#seperating mydata in ',' and storing the results in a list
list = mydata.split(',')

#storing in round the first element of the list which is the round number of mydata and seperating it in words and numbers 
round = list[0].split(':')

#keeping only the number which is stored in the second cell of the list round and making it an integer 
roundNumber = round[1]
roundNumber = int(roundNumber)

#storing in randomness the first second of the list which is the randomness of mydata and seperating it in words and numbers 
randomness = list[1].split(':')

#keeping only the number which is stored in the second cell of the list randomness and making it an integer 
randomnessNumber = randomness[1]
randomnessNumber = str(randomnessNumber)

#turing the randomness number in binary
binaryRandomness = ''.join(format(ord(i), '08b') for i in randomnessNumber)

#storing in a variable the first binary randomness number 
binaryText = binaryRandomness

#executes the code for the previous 99 rounds 
for i in range(1,100):
    
    roundNumber = roundNumber - 1
    
    req = Request('https://drand.cloudflare.com/public/'+str(roundNumber), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    
    mydata = str(data)
    list = mydata.split(',')

    randomness = list[1].split(':')
    randomnessNumber = randomness[1]
    randomnessNumber = str(randomnessNumber)

    binaryRandomness = ''.join(format(ord(i), '08b') for i in randomnessNumber)

    #storing in binaryText each binary randomness number
    binaryText += binaryRandomness

#seperates binaryText in '1' and stores the results in a list in order to keep all the 0s in a sequence
separatedZeros = []
separatedZeros = binaryText.split('1')
maxZero = 0 

#searches for the longest sequence of 0s in the list 
for i in range(len(separatedZeros)):
    if len(separatedZeros[i]) > maxZero:
        maxZero = len(separatedZeros[i])

#seperates binaryText in '0' and stores the results in a list in order to keep all the 1s in a sequence
separatedOnes = []
separatedOnes = binaryText.split('0')
maxOne = 0 

#searches for the longest sequence of 1s in the list 
for i in range(len(separatedOnes)):
    if len(separatedOnes[i]) > maxOne:
        maxOne = len(separatedOnes[i])

print("The largest sequence of zero's (0) is:", maxZero)
print("The largest sequence of one's (1) is:", maxOne)