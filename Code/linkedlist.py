#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?
        O(n) because we have to traverse every single node.
        """
        # TODO: Loop through all nodes and count one for each
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list. """
        # TODO: Create new node to hold given item
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        # TODO: Else append node after tail
        
        # create new node for item
        new_node = Node(item)
        # if head is empty
        if self.is_empty() == True:
            # set the head and tail to new node
            self.head = new_node
            self.tail = new_node
            # print(new_node)
        else:
            # append node
            self.tail.next = new_node
            self.tail = new_node
            print(self.tail.next)


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?
        O(1) because we already have reference to the head, just point the new node's next to the existing head.
        """
        # TODO: Create new node to hold given item
        node = Node(item)
        # check if node exists
        if self.tail == None:
            # set head and tail to new node
            self.head = node
            self.tail = node
        else:
            # assign head to next node
            next_node = self.head
            self.head = node
            self.head.next = next_node

    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        O(1), the item is the first node (head) or last node (tail) in which we can check first
        TODO: Worst case running time: O(???) Why and under what conditions?
        O(n), the item is the 2nd to last node, so we had to traverse the entire list.
        """
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        node = self.head
        if node.data == item or self.tail.data == item:
            return True
        node = node.next
        while node is not None:
            if node.data == item:
                return True
            node = node.next
        return False

    def find_if_matches(self, matching_function):
        """Return an item from this linked list if it is present."""
        node = self.head
        while node:
            if matching_function(node.data): 
                return node.data
            node = node.next
        return None # Nothing satisfied the matching function

    def find_and_return_node(self, matching_function):
        """Return an item from this linked list if it is present."""
        node = self.head
        while node:
            if matching_function(node.data): 
                return node
            node = node.next
        return None # Nothing satisfied the matching function

    def delete(self, item):
        if self.length():
            curr_node = self.head
            # Checks if the head node is the item
            if curr_node.data == item:
                # when there is only 1 node you want to set tail and head to equal NONE
                if curr_node == self.tail:
                    self.tail = None
                self.head = curr_node.next
                # return nothing
                return

            # Keep looping through nodes until value is found
            # This will only exit if value is found or the current_node.next == None
            runner = curr_node.next
            while runner and runner.next:
                if runner.data == item:
                    curr_node.next = runner.next
                    return
                curr_node = curr_node.next
                runner = runner.next

            # This will always run when the above while loop has broken
            # meaning the current_node.next was equal to NONE
            # this also means you're at the last node
            if runner.data == item:
                curr_node.next = None
                self.tail = curr_node
                return

        raise ValueError('Item not found: {}'.format(item))


if __name__ == "__main__":
    my_ll = LinkedList(["A", "B", "C"])
    print(my_ll)

    

