for i in range(10):
    print(i)
    
print("\nLoop completed.")
print("\n")
for j in range(5, 15):
    print(j)
    
print("\nSecond loop completed.")
print("\n")
for k in range(2, 20, 3):
    print(k)

print("\nThird loop completed.")
print("\n")

list1 = list(range(10))
print("List created from range:", list1)

set1 = set(range(5, 15))
print("Set created from range:", set1)

dict1 = {i: i * 2 for i in range(5)}
print("Dictionary created from range:", dict1)
tuple1 = tuple(range(3, 10))
print("Tuple created from range:", tuple1)

