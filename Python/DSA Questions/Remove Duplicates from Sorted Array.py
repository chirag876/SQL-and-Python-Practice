lst = [0,0,0,1,1,2,3,4,4,5,6,7,7,8,8]
non_duplicatedvalues = []
count = 0 
for i in lst:
    if i not in non_duplicatedvalues:
        non_duplicatedvalues.append(i)
    else:
        count+=1
print(non_duplicatedvalues)
print(count)
        