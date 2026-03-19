# Create a list of squares from 1 to 10
squares = [i*i for i in range(1, 11)]
print("Squares:", squares)

# List of powers of 2 from 2^1 to 2^5
val = [2**i for i in range(1, 6)]
print("Powers of 2:", val)

# List of even numbers from the squares list
val2 = [i for i in squares if i % 2 == 0]
print("Even squares:", val2)

#Dictionary comprehension
squares={x:x*x for x in range(1,6)}
print(squares)

doubles={x:2*x for x in range(1,6)}
print(doubles)
