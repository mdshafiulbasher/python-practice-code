
# 01. remove duplicates from a list.
list1 = [2,5,4,2,6,7,5,1]
newList = []
for num in list1:
    if num not in newList:
        newList.append(num)
print(newList)

# 02. check if a list is empty or not.
list2 = []
if len(list2) > 0:
    print('this list is not empty')
else:
    print('this list is empty')

# 03.clone or copy a list.
list3 = [3,6,5,2,1,7,4]
newList2 = list3.copy()
print(newList2)

# 04. convert a list of characters into a string.
list4 = ["a","b","c","d"]
s=""
for x in list4:
    s=s+x
print(s)

