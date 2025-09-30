"""
Create a nested list named nested_list with at least two inner lists.
Make a shallow copy of nested_list and assign it to shallow_nested_copy.
Make a deep copy of nested_list and assign it to deep_nested_copy.
Modify an element in one of the inner lists of shallow_nested_copy.
Modify an element in one of the inner lists of deep_nested_copy.
Print all three lists and explain the differences. 
"""
import copy

nested_list = [[1, 2, 3], [5, 6, 7]]  # making the original list
# using copy.copy to make a shallow copy
shallow_nested_list = copy.copy(nested_list)
# using copy.deepcopy to make a deep copy.
deep_nested_list = copy.deepcopy(nested_list)

nested_list[0].append(20)

shallow_nested_list[0].append(4)  # appending 4 to the end of index 0's list

deep_nested_list[1].insert(0, 4)  # adding 4 to the start of index 1's list

print(
    f"\nOriginal: {nested_list}\n"
    "The original copy remains unchanged after it's own append.\n\n"
    f"Shallow Copy: {shallow_nested_list}\n"
    "The shallow copy recieves it's own append as well as the one done to the original because it references it.\n\n"
    f"Deep Copy: {deep_nested_list}\n"
    "The deep copy only recieves the modification done to it itself because it is a completely seperate copy.\n"

)
