from turtle import done


def goodDay(name,ending):  #function defination with arguments
    print("Good Day", name, ending)

goodDay("himanshu", "Thank you!")  #function call with arguments
goodDay("himanshu", "Have a nice day!") 
goodDay("himanshu", "Good luck!")


#function arguments with return value
def goodDay(name,ending):  #function defination with arguments
    print("Good Day", name, ending)
    return 7

a = goodDay("himanshu", "Thank you!")  #function call with arguments
print(a)