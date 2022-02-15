import random

victory=0
sum=0
ring=[1,2,3]
places= [0,1,2,3,4,5,6,7,8]
#plays the game 100 times
for k in range (100):

    steps = 0
    flag = False
    table = [0] * 9

    #the maximum steps are 27
    for j in range (27):

        #increases the steps variable every time and chooses a random ring out of the 3 sizes 
        steps+=1
        randomRing = random.choice(ring)

        #chooses a random place in the table to place the ring 
        while flag == False:
            a = random.choice(places)
            if table[a] != randomRing: 
                table[a] = randomRing 
                flag = True
            else:
                randomRing = random.choice(ring)

        flag = False

        #checking if the game has come to an end if there have been made more than 3 steps
        if steps>=3:
            for i in range (3):

                #checks for a win vertically for the same size rings and different size rings 
                if table[i] == table[i+3] == table[i+6] or (table[i] ==1 and table[i+3] ==2 and table[i+6] == 3) or (table[i] ==3 and table[i+3] ==2 and table[i+6] == 1):
                    sum=sum+j
                    victory +=1
                    flag = True

                #checks for a win horizontally for the same size rings and different size rings 
                if table[i]==table[i+1]==table[i+2] or (table[i] ==1 and table[i+1] ==2 and table[i+2] == 3) or (table[i] ==3 and table[i+1] ==2 and table[i+2] == 1):
                    sum=sum+j
                    victory +=1
                    flag = True
            
            #checks for a win diagonally for the same size rings and different size rings
            if table[0]==table[4]==table[8] or (table[0] ==1 and table[4] ==2 and table[8] == 3) or (table[0] ==3 and table[4] ==2 and table[8] == 1):
                sum=sum+j
                victory +=1
                flag = True

            #checks for a win diagonally for the same size rings and different size rings 
            if table[2]==table[4]==table[6] or (table[2] ==1 and table[4] ==2 and table[6] == 3) or (table[2] ==3 and table[4] ==2 and table[6] == 1):
                sum=sum+j
                victory +=1
                flag = True

        if flag == True:
            break

sum=sum/100
print(sum)