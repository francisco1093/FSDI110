#description
"""
PyCal:Simple calculator
Author: Francisco Cardenas
Date: June 2021
Functionality:
    -simple mathematical operation
"""
#import

#globals

#funtions

def print_menu():
    print(" -------------------")
    print("| Welcome to PyCalc |")
    print(" -------------------")

    print("1 - Sum")
    print("2 - Subtract")
    print("3 - Multiplicacion")
    print("4 - Division")
    print("5 - Is it odd ?")
    print("6 - Print a message N times")

    print("q - Quit")

    print("----------------")

def clear():
    print("\n\n\n\n\n")

selected_option=""
while (selected_option!="q"):
    clear()
    print_menu()
    invalid_option=True
    while(invalid_option):
        selected_option = input("Select an option: ")
        if selected_option not in ("1","2","3","4","5","6","q"):
            print("Please select a valid option \n")
        else:
            invalid_option=False



    if(selected_option=="q"):
        break
    if(selected_option!="6"):
        num1=float(input("provide num1: "))
        if(selected_option!="5"):
            num2=float(input("provide num2: "))

    if(selected_option == "1"):
        print(f"The result is:{num1+num2} ")
    elif(selected_option == "2"):
        print(f"\nThe result is:{num1-num2}")
    elif(selected_option == "3"):
        print(f"The result is:{num1*num2}")
    elif(selected_option=="4"):
        if(num2==0):
            print("Error: Division by zero is not allowed")
        else:
            print(f"The result is:{num1/num2}")
    elif(selected_option=="5"):
        if (num1 % 2) == 0:  
            print("{0} isnt Odd number".format(int(num1)))  
        else:  
            print("{0} is Odd number".format(int(num1))) 
    elif(selected_option=="6"):
        msg = input("Write message: ")
        count = input("Number of times: ")
        for i in range(int(count)):
            print(msg) #print(msg, end=" ") print in same line 


    input("\nPress Enter to continue...")

print("Good Bye!!")

    
    


#instructions



