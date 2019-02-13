while True:
    value=input("Integer between 1 and 100:")
    try:
        value=int(value)
    except ValueError:
        print("No valid number")
        continue
    if 0<=value<=100:
        break
    else:
        print("Invalid range")
for x in range(1, value + 1):
        if x % 3 == 0 and x % 5 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        else:
            print(x)

