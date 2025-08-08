# Break example

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)
    
print("Loop ended because of break statement")

# Continue example
for num in numbers:
    if num == 3:
        continue
    print(num)
    
print("Loop continued because of continue statement")