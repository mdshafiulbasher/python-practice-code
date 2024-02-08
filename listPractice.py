# sum of list
num1 = [12, 25, 65, 85,100]
sum = 0
for num in num1:
    sum = sum+num
print(sum)

# multiply of list
num2 = [1,2,3,4,5]
multiply = 1
for num in num2:
    multiply=multiply*num
print(multiply)

# largest number of the list
num3 = [65,87,12,49,34,10]
max = num3[0]
for num in num3:
    if num>max:
        max=num
print(max)

# smallest number of the list
min=num3[0]
for num in num3:
    if num<min:
        min=num
print(min)