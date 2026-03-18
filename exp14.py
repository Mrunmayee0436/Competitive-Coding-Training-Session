n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    val = int(input("Enter element: "))
    arr.append(val)

total = 0
for i in arr:
    total = total + i

print("Array elements =", arr)
print("Sum of array elements =", total)