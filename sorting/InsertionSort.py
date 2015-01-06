import random

#Insertion sort
def insertion_sort(items):
    n = len(items)
    for index in range(1, n):
        sub_index = index

        temp = items[index]          
        while sub_index > 0 and items[sub_index - 1] > temp:
            items[sub_index] = items[sub_index - 1]
        
            sub_index -= 1
        items[sub_index] = temp
    return items
    
items = random.sample(range(0, 10), 10)
print str(items)[1:-1]
insertion_sort(items)
print str(items)[1:-1]