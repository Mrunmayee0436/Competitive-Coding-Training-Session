def searchValue(target):
    for i in range(len(mylist)):
        if mylist[i] == target:
            return i
        
mylist = [4,2,7,8,5,4,1]
target = 7
res = searchValue(target)
print("Value found at index number =",res)