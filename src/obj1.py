arr = [12, 23, 45, 1, 4, 7, 67]

# Lookup
def lookup_item_by_index(array, index):
    # To look up an item by index in an array is constant time O(n)
    return array[index]

# Append
def add_item_to_end(array, item):
    # adding an item to the end of an array is constant time O(n)
    array.append(item)

# Insert
def insert_item_at_index(array, index):
    pass

print(lookup_item_by_index(arr, 1))

print(arr)
add_item_to_end(arr, 44)
print(arr)