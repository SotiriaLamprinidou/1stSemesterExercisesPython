from urllib.request import Request, urlopen
from scipy.stats import entropy as en
import pandas as pd


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

#keeping only the number which is stored in the second cell of the list randomness and making it a string
randomnessNumber = randomness[1]
randomnessNumber = randomnessNumber.replace('"',"")
randomnessNumber = str(randomnessNumber)

#storing in a variable the first hex randomness number 
hexText = randomnessNumber

#executes the code for the previous 19 rounds 
for i in range(1,20):
    
    roundNumber = roundNumber - 1
    
    req = Request('https://drand.cloudflare.com/public/'+str(roundNumber), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    
    mydata = str(data)
    list = mydata.split(',')

    randomness = list[1].split(':')
    randomnessNumber = randomness[1]
    randomnessNumber = randomnessNumber.replace('"',"")
    randomnessNumber = str(randomnessNumber)

    #storing in hexText each hex randomness number
    hexText += randomnessNumber
    

# Python code to convert string to list character-wise

list1=[]
list1[:0]=hexText

#calculating the entropy
pdSeries = pd.Series(list1)
entropy = en(pdSeries.value_counts())
print(entropy)