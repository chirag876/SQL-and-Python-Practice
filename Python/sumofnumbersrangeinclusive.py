def sumofnumbers():
    sum = 0
    startnumber = 25
    for i in range(startnumber, 76):
        sum += i
    return sum


print("sum:", sumofnumbers())
