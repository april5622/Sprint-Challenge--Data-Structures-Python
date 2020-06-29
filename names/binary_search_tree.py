class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the new value we want to insert
        if value < self.value:
             # if new value < self.value
          # IF, self.left is already taken by a node,
            # make that left node, call insert
          # set the left to the new node with the new value
            if self.left is None:
                self.left = BSTNode(value) # this will replace the current left node and we dont want that
            else:
                self.left.insert(value) # recursion 
                
        if value >= self.value:
            # if new value >= self.value 
            # IF, self.right is already taken by a node,
                # make that right node, call insert
            # set the right child to the new node with the new value
            if self.right is None: # if there is no node there, have that current right subroot node decide...
                self.right = BSTNode(value) #...where to put the new value
            else:
                self.right.insert(value) # if the value is greater than the current, it will be inserted there
            

     # Return True if the tree contains the value
     # False if tree does not contain value
    def contains(self, target):
        # if current self.value == target:
        if self.value == target:
            # return True
            return True
        # compare the target to current value
        # if current self.value is more than target
        if self.value >= target:
            # check the left subtree
            if self.left is None: # left subtree not there
                # if cannot go left, return False
                return False
            found = self.left.contains(target) # recursion state
            
        # if current self.value is less than target
        if self.value < target:
            # check the right subtree contains target
            if self.right is None: # right subtree not there
                # if you cannt go right, return False
                return False
            found =  self.right.contains(target) # recursion state
         # return if found since its true that in the recursion, it did contain the target
        return found


    # Return the maximum value found in the tree
    def get_max(self):
        # Keep moving to the right if current root node is not max since max node goes rightmost
        if not self.right:
            return self.value
        return self.right.get_max() # recursion to get the max in the rightmost


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function on the current value fn(self.value)
        fn(self.value)
        # if you can go left, call for_each on the left tree
        if self.left:
            self.left.for_each(fn)
        # if you can go right, call for_each on the right tree
        if self.right:
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node): # very similiar to for_each function
        # print left then node then right
        # lowest value in the left first then root and then greatest value in the right
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes
        queue = []                 
        # add the first node to the queue
        queue.append(self) 
        # while queue is not empty
            # remove the first node from the queue
            # print the remove node (Parent nodes are printed before children since its going in a wave)
            # add all children into the queue
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node): # this is like for_each function of printing
        # create a stack for nodes
        stack = []
        # add the first node to the stack
        stack.append(self)
        # while stack is not empty
            # get current node from the top of stack
            # print node remove from stack from top to bottom
            # add all the children to that stack 
            # keep in mind, the order you add the children will matter. greatest to smallest
        while len(stack) > 0:
            current_node = stack.pop(len(stack)-1)
            print(current_node.value)
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left) 
       

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(self.value)
        if self.left:
            self.left.pre_order_dft(self) 
        if self.right:
            self.right.pre_order_dft(self)
        

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if self.left:
            self.left.post_order_dft(self)
        if self.right:
            self.right.post_order_dft(self)
        print(self.value)