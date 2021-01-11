#Question 2
#pennies for pay.py
#Franck haba
#b00125589
#15/12/20

print("\nThis programe is to calculate the amount of money a person would earn over a period of time if his or her salary is one penny the first day,two pennies the second day,and continuesto double each day\n")

name = input(" Enter your name please: ")

def main():


 


 try:
          print()
          number_of_days_worked = int(input(" Please insert the number of days you worked:\n"))



 except ValueError:
          print()
          print("Error please leave out letters!!!!!!!\n")
          
          restart = number_of_days_worked = int(input(" Please insert the number of days you worked:\n"))

 

 
 pay_per_day = 0.01
 
 number_of_all_pennies = 0

 penies = .01


 print("Day\t pennies \n")
 for presentday in range(number_of_days_worked):
     pennies_per_day = 2** presentday
     number_of_all_pennies = number_of_all_pennies =+ pennies_per_day
     
     print(presentday +1,"\t",pennies_per_day , "\n" )



 total_amount =  number_of_all_pennies *  penies

 print( f"{name} total amount is: $", total_amount)


main()


