class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node


class SinglyLinkedList(object):

    def __init__(self, head):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                return current
            else:
                current = current.get_next()
        if current is None:
            raise ValueError('%s not in list')

    def traverse(self):
        current = self.head
        print('Head of linked list')
        while current:
            print('This node has data of %s' % current.get_data())
            current = current.get_next()
        print('End of linked list')
        return

    def delete(self, data):
        current = self.head
        previous = Node
        while current:
            if current.get_data() == data:
                if previous:
                    previous.set_next(next_node=current.get_next())
                else:
                    self.head = current.get_next()
            previous = current
            current = current.get_next()
        if current is None:
            raise ValueError('%s not in list' % data)


if __name__ == '__main__':
    print('Create singly linked list')
    node1 = Node(data=1)
    print('Node 1 has data of %s' % node1.get_data())
    if not node1.get_next():
        print('Node 1 does not have any next node')
    node2 = Node(data=2)
    print('Node 2 has data of %s' % node1.get_data())
    if not node1.get_next():
        print('Node 2 does not have any next node')
    # Create a singly linked list with node 1 as head
    singly_linked_list = SinglyLinkedList(head=node1)
    # Insert data
    singly_linked_list.insert(data=2)
    singly_linked_list.insert(data=3)
    # Search for 2
    found_node = singly_linked_list.search(data=2)
    if found_node:
        print('This node has data of %s' % found_node.get_data())
    # Traverse
    singly_linked_list.traverse()
    # Delete node 2
    singly_linked_list.delete(data=2)
    singly_linked_list.traverse()
