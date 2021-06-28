# first in first out
# ENQUEUE ADD ITEMS && DEQUEUE REMOVE ITEMS
# placing order is appn of queue

# queue using python Deque
from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())
print(my_queue)
