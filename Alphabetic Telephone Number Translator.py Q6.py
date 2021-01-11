#exercise 6
#franck haba
#b00125589
#30/12/20
#Alphabetic Telephone Number Translator


def main():
 companyname= input(' please enter company name please:\n')
 phoneNum = input("Enter the number in the format of 555-GET-FOOD:\n ")
 
def phoneNumber():
    phoneNum.split('-')
    areacode=num[0]
    numend=num[1:]
    number=""

    for n in numend:

     for i in range (len(n)):
         if n [i] in 'a' or 'b'or 'c':
             number=number+'2'
         elif n [i] in 'a' or 'b' or 'c': 
          number=number+'3'
         
         elif n [i] in 'd' or 'e' or 'f':
          number=number+'4'    

         elif n [i] in 'g' or'h' or' i':
          number=number+'5'
         elif n [i] in 'j' or'k'or'l':
           number=number+'mno'
         elif n [i] in 'p' or 'q' or 'r' or 's':
           number=number+'7'
         elif n [i] in 't' or 'u' or'v':
           number=number+'8'
         elif n [i] in 'w' or 'x' or 'y'or'z':
          number=number+'9'
          number=number+'-'
         return areacode+'-'+number[:1]
 
      
          
            
 
print(phoneNumber)
               
            

main()

def exit():
    choice=""

    while choice != "exit":

             choice = input("please enter exit to leave program:\n")
    print (choice)
    exit()
    

 
