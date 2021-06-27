# Dictionaries are unordered
# # key value pair
# # associative array like java hashmap

# Define
x = {'one': 1, 'two': 2}
# or giving tuples in pairs
# or
y = dict(one=1, two=2)

y["three"] = 3
print(y)

for k, v in y.items():
    print(k, v)
