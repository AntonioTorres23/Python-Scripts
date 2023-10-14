'''
Calculator in Python3
Coded by Antonio Torres and Parke Lovett
Version 1.0 
Revisions to continue game logic from a function to a while True loop to clean up code

'''


def addition(a,b):
    return (a+b)
    
    
def subtraction(a,b):
    return a-b
    
    
def multiplication(a,b):
    return a*b

    
def division(a,b):
    return a/b


def exponent(a,b):
    return a**b
    
    
def game():
    a = float(input("Enter a number: "))
    opp = input("Enter an operator (+,-,/,*,**): ")
    b = float(input("Enter another number: "))
    addition_var = '+'
    subtraction_var = '-'
    multiplication_var = '*'
    division_var = '/'
    exponent_var = '**'
    if opp == addition_var:
        print(addition(a,b))
    elif opp == subtraction_var:
        print(subtraction(a,b))
    elif opp == multiplication:
        print(multiplication(a,b))
    elif opp == division_var:
        print(division(a,b))
    elif opp == exponent_var:
        print(exponent(a,b))
    else:
        print ("Incorrect Syntax")
    while True:
        go_again=input("would you like to go again? y/n ")
        
        if go_again == 'y' or go_again == 'Y':
            game()
            break
        elif go_again == 'n' or go_again == 'N':
            break
        
game()
        
