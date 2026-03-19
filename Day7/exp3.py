#input= mrunmayee is a good programmer
#WAP to count the word
#output = 4
name ="mrunmayee is a good programmer"
count =1
for i in name:
    if i == " ":
        count += 1
    else:
        continue
print("Total word count =",count)
