#nested function

def outerFunction():
    print("This is my outer function:") #second
    def innerFunction():
        print("inner Function")
    innerFunction() #third execution
outerFunction() #First execution starts from here
