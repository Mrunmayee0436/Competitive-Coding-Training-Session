def searchValue(mylist):
    sum = 0
    for i in range(len(mylist)):
        sum = sum + mylist[i]
    return sum

mylist = [4, 2, 7, 8, 5, 4, 1]
res = searchValue(mylist)   # calling function
print("Sum of array =", res)