# Function
def msg():
    val1 = int(input("Enter first value: "))
    val2 = int(input("Enter second value: "))

    sum = val1 + val2
    mul = val1 * val2
    sub = val1 - val2
    div = val1 / val2

    return (sum, mul, sub, div)   # returning tuple

res = msg()
print("Result =", res)