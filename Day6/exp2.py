myList = []
total = 0

N = int(input("Enter the value of N: "))

for i in range(N):
    val = int(input("Enter the value: "))
    myList.append(val)

for j in range(len(myList) - 1):  # loop till second last element
    total += abs(myList[j] - myList[j + 1])

print("Total distance:", total)
