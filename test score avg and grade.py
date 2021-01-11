#Questions 3
#test avg n grade
#franck haba
#b00125589
#25/12/20

def enterstudentname(name):
 name = input("\n please Enter student name:\n ")
 
def cal_average(studentscore):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg



def ca_average(score1, score2, score3, score4 ,score5 ):
   average = (score1 + score2 + score3 + score4 + score)/5
   return average

def grade( studentscore ):

 if( studentscore <= 100):
    return "A"
 elif( studentscore < 90):
     return "B"
 elif( studentscore < 80):
     return "C"
 elif( studentscore < 70):
     return "D"
 elif( studentscore < 60):
     return "F"


def askforscores():
    socre1=float(input("please enter score1: "))
    socre2=float(input("please enter score2: "))
    socre3=float(input("please enter score3: "))
    socre4=float(input("please enter score4: "))
    socre5=float(input("please enter score5: "))
    
    return score1, score2, score3, score4, score5

def printscores(score1, score2, score3, score4, score5):

    print("score\tletter grade\n")
    
    print(str(score1) + "\t" + grade(score1),\
          str(score2) + "\t" + grade(score2),\
          str(score3) + "\t" + grade(score3),\
          str(score4) + "\t" + grade(score4),\
          str(score5) + "\t" + grade(score5) )

def main():
    name = input("\n please Enter student name:\n ")
    school=input("\n please Enter school:\n ")
    studentnumber=input("\n please Enter student number:\n ")
    studentname= ("student should enter name and student number:")
    
    score1, score2, score3, score4, score5 = askforscores()

    printscores(score1, score2, score3, score4, score5)

main()
choice=""

while choice != "exit":

    choice = input("please enter exit to leave program:\n")
    print (choice)
    exit()               









