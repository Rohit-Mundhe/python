# tuples are immutable ( CAN'T ADD OR CHANGE)
# USEFUL FOR FIXED DATA
# FASTER THAN LIST
# SEQUENCE TYPE


# DEFINE
#X = ()
X = (1, 2)
t = 1, 2, 3, 4
y = 2,

list1 = [2, 4, 8]
z = tuple(list1)

# del, x[1]=8 fails for tuples

# Concatenate works!
y += (4,)


# sets very fast than list
# set is not ordered
set1 = {2, 4, 10}
y = set()
y = set(list1)
# adding element y.add(item)  ,, removing y.remove(item)
y.pop()
print(y)

print(y.pop(), y)  # popping random item

# we perform sets operation on two sets & intersection, | union, ^, -, <=or >= to check subsets
