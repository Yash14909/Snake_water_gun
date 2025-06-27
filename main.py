import random
'''
1=snake
-1=wate
0=gun
'''
computer = random.choice([-1,0,1])
youStr = input("Enter your choice:")
yrDict ={"s":1,"w":-1,"g":0}
you=yrDict[youStr]
reverseDict={1:"s",-1:"w",0:"g"}
# By now we have two variables computer and you

print(f"Your choice is {reverseDict[you]} and computer choice is {reverseDict[computer]}")

if(computer==you):
    print("It's a draW!")
else:
    #if((computer-you)==-1 or (computer-you)==2):
         # print("You lose!")
    #else:          
            #print("You won!")
    if(computer ==-1 and you==1): #-2
          print("You won!")
    elif(computer ==-1 and you==0): #-1
          print("You lose!")
    elif(computer ==1 and you==-1): #2
          print("You lose!")
    elif(computer ==1 and you==0): #1
          print("You won!")
    elif(computer ==0 and you==1): #1
          print("You lose!")
    elif(computer ==0 and you==-1): #-1
          print("You won!")
    else:
          print("Something went wrong!")    




