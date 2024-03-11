numbers = [5, 6, 7, 4, 3, 5, 4, 8, 5, 8, 9]

new = []
for i in numbers:
     if i not in new:
         new.append(i)
print(new)