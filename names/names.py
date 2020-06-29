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
# RUNTIME is 6.58940315246582 seconds
# TIME COMPLEXITY: 0(n^2)

#for name_1 in names_1: # O(n)
#    for name_2 in names_2: # O(n)
#        if name_1 == name_2: # O(1)
#            duplicates.append(name_1) # O(1)

# IMPROVED 
# Runtime: 0.13575196266174316 seconds

BST = BSTNode("names")

for i in names_1: # O(n)
    BST.insert(i) # O(log(n))

for i in names_2: # O(n)
    if BST.contains(i): # O(1)
        duplicates.append(i) # O(log(n))

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
