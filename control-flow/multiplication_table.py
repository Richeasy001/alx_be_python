number = int(input("Enter a number to see its multiplication table: "))
for y in range(1, 11):
    result = number * y
    print(f"{number} * {y} = {result}")