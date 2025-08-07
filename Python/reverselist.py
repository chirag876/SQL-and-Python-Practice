mylist1 = [1, 2, 3, 4, 5]
reverserlist = mylist1[::-1]  # Reverse the list
print("Reversed list:", reverserlist)


mylist1.reverse()  # Reverse the list in place
print("Reversed list 2:", mylist1)

mylist2 = [6, 7, 8, 9, 10]
reverserlist2 = list(reversed(mylist2))  # Reverse the list using the reversed() function
print("Reversed list 3:", reverserlist2)
