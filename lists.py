def get_n_values(n):
    for m in range(n):
        try:
            result.append(int(input('Enter an element: ')))
        except ValueError:
            print("Invalid data. Elements must be natural numbers")
            quit()
    return result


result = []
try:
    n = int(input("Enter the number of elements in a list: "))
except ValueError:
    print("Invalid data. The number of elements must be natural ")
    quit()
if n != 0:
    get_n_values(n)
    count = 0
    delta = input("Enter the value of DELTA: ")
    try:
        delta = int(delta)
    except ValueError as message:
        print("Invalid data. DELTA must be a natural number or zero")
    if int(delta) >= 0:
        minim = result[0]
        for i in range(1, len(result)):
            if result[i] < minim:
                minim = result[i]
        for x in result:
            if x - minim == delta:
                count += 1
        if delta == 0 and count >= 2:
            count -= 1
        print(f"The number of such elements in the list equals {count}")
    else:
        print("Invalid data. Enter a proper value of DELTA")
        quit()
else:
    print("Invalid data. The number of elements should be natural")
    