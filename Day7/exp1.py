#WAP to perform arithmatic operation using functional programming approach
#Functions helps us to acheive modularity approach
import sys

# Function definitions
def addition(num1, num2):
    print("Addition =", num1 + num2)

def subtraction(num1, num2):
    print("Subtraction =", num1 - num2)

def multiplication(num1, num2):
    print("Multiplication =", num1 * num2)

def division(num1, num2):
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Error: Division by zero is not allowed!")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = int(input("Enter your choice from above options: "))
    
    if choice == 5:
        print("Exiting program...")
        sys.exit()  # Exit the program
    
    val1 = int(input("Enter first value: "))
    val2 = int(input("Enter second value: "))
    
    if choice == 1:
        addition(val1, val2)
    elif choice == 2:
        subtraction(val1, val2)
    elif choice == 3:
        multiplication(val1, val2)
    elif choice == 4:
        division(val1, val2)
    else:
        print("You have entered wrong choice")
