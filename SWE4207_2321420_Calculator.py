
def calculator(): # i decided to make a define function for the calculator to be in to so it can loop after the user recieves an answer inside 
    global firstnum,secondnum,operation,calculator # this is for these variables to be used all over the code so it can be used anywhere
    print('Welcome to my calculator') # welcome message

    firstnum =int(input('Enter your first number \n')) # heres is where the user enters the first number
    secondnum = int(input('Enter your second number \n')) # here is where the user enters the second number
    operation = input('Please enter one of the following + - / *\n') # here is the where the operation between the numbers is inserted 


    if operation == '+':
        print(firstnum + secondnum) #this is if the user inserts addition which is equal to what the if statement is requesting
        calculator() # this the calculator in a define function so the process will begin again
    elif operation == '-':
        print(firstnum - secondnum) #this is if the user inserts subtraction which is equal to what the if statement is requesting
        calculator()  # this the calculator in a define function so the process will begin again
    elif operation == '/':
        print(firstnum / secondnum) #this is if the user inserts divide which is equal to what the if statement is requesting
        calculator()  # this the calculator in a define function so the process will begin again
    else:
        print(firstnum * secondnum) #this is if the user does none of the following so multiplication is left
        calculator()  # this the calculator in a define function

calculator() # here is calculation in a define function again so it will loop and the user can do this as many  times as they like



# step 1 make a space for the user to enter their numbers
# step 2 allow the users to put the symbols for the operation they want completed with the numbers
# step 3 when the code is run the collected answer from these numbers should be displayed
