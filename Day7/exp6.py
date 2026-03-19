# Removing spaces from the string
# 1. rstrip() => removes spaces on the right
# 2. lstrip() => removes spaces on the left
# 3. strip()  => removes spaces from both sides

city = input("Enter your city Name: ")
scity = city.strip()  # Removes leading and trailing spaces

if scity == 'Hyderabad':
    print("Hello Hyderabadi.. Adab")
elif scity == 'Chennai':
    print("Hello Madrasi... Vanakkam")
elif scity == "Bangalore":
    print("Hello Kannadiga... Shubhodaya")
else:
    print("Your entered city is invalid")
