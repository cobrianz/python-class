""" names = ['john','fred','mary','Edwin']
print(names[2:])
print(names[:1])  """
numbers = [10,20,30,40,50,60,70,80,90]
largest = 0

for number in numbers:
    if number > largest:
        largest = number
print(largest)