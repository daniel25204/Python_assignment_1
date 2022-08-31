largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = float(num)
        except:
            print("Please enter a number...")
            continue
        if largest == None and smallest == None:
            largest = num
            smallest = num
        elif num > largest:
            largest = num
        elif num < smallest:
            smallest = num 
                   
print("Maximum", int(largest))
print("Minimum", int(smallest))