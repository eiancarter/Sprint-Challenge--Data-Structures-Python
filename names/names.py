import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# Step 1 - set the first index of names (either list) as the root node of a BST 
bst = BSTNode(names_1[0])
## bst runtime is 0.14s
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2):
        duplicates.append(name_2)

## easier preferred method using set() runtime of 0.005s because a set is constant look up time
# therefore - O(n) time and O(n) space
# set_names_1 = set(names_1)
# for name_2 in names_2:
#     if name_2 in set_names_1:
#         duplicates.append(name_2)
        


# I have decoupled the lists so there are no longer any nested for loops, 
# and I'm only traversing the bst and names_2 list once in order to check each value
# so my time complexity is O(2N) or O(N). My space complexity is O(H), because worst
# case I have to traverse the entire tree and I have an empty list duplicates which is also O(N)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")



##current runtime: 8.9 sec

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
