import random

#Insertion sort
def selection_sort(items):
    n = len(items)
    
    for i in range(0, n):
        min_index = i
        # find the minimum value
        for j in range(i+1, n):
            if items[j] < items[min_index]:
                min_index = j
        # swap values. only if minimum value is found
        if min_index != i:
            temp = items[min_index]
            items[min_index] = items[i]
            items[i] = temp
            
    return items
    
items = random.sample(range(0, 10), 10)
print str(items)[1:-1]
selection_sort(items)
print str(items)[1:-1]