#Question 4
#Random Number File Writer
#27/12/20
#Franck haba
#b00125589

import random

def genraterandomnumber():
    randomnumber = random.randint(1, 100)
    return randomnumber

def main():
    print("This program is to genrate random numbers\n")
    
    name = input("\n Please enter name:\n ")
    try:
        random_num = int(input("How many number should the file hold?:\n"))


        file=open("randomnumbers.txt","w")
    except ValueError:
       print("Error please input numbers only\n")

       restart= random_num = int(input("How many number should the file hold?:\n"))
       file=open("randomnumbers.txt","w")
         
    for randomnumbercount in range (1, random_num + 1):
       randomnumber = genraterandomnumber()
       file.write(str(randomnumber) + "\n")

       
            

      
main()

print( "\nType Exit to kill program\n")

choice=""

while choice != "exit":

    choice = input("please enter exit to leave program:\n")
    print (choice)
    exit()                      
    


