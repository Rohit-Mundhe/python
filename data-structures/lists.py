# LIST general purpose data structure

# defining
x = list()

y = [1, 2]

t = (1, 2)
z = list(t)

b = [i**2 for i in range(1, 11)]  # list comprehension
print(b)
del(b[1])
print(b)

b.append(121)
print(b)

ylist = [144, 169]
b.extend(ylist)  # similar to add
print(b)

b.insert(1, 2)
b.pop()
b.remove(144)
print(b)

b.reverse()
print(b)

# SORTED CREATES NEW LIST IN SORTED ORDER SORT REARRANGE LIST IN ORDER
b.sort()
print(b)
