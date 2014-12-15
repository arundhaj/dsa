import random

# Bubble sort
def bubble_sort(items):
    n = len(items)
    i = 1
    while i <= n:
        j = 0
        while j < (n - i):
            if items[j] > items[j + 1]:
                # swap elements
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp
            j += 1
        i += 1
    
    return items

items = random.sample(range(0, 10), 10)
print str(items)[1:-1]
bubble_sort(items)
print str(items)[1:-1]