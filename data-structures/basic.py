# string

# slicing can be done in list string and tuples also
x = 'Hello'
print(x[3])
print(x[1:4])
print(x[2:])
print(x[:4])
print(x[:-2])
print(x[-1])
print(x[-0])
# string operations
y = x+"world"
print(y)
# list
z = ["pig", "chicken"] + ["tiger"]
print(z)

# tuples
t = ("kevin", "rock", "robert") + ('chris',)  # comma is very important
print(t)

listy = [2, 4, 6]
for index, item in enumerate(listy):
    print(index, item)

print(min(listy))
print(max(t))
print(sum(listy[1:]))
print(sorted(t))

# print in sorted order in referece to second elment
print(sorted(t, key=lambda k: k[1]))

print(x.count('l'))
print(t.index("rock"))


# unpacking
a, b, c = listy
print(a, b, c)
print(listy[1:])
print(t[1:])
