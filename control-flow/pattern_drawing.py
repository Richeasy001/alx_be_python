square = abs(int(input("Enter the size of the pattern: ")))
j= 1
while j <= square:
    i = 1
    while i <= square:
        print ("*", end="")
        i += 1
    print()
    j += 1