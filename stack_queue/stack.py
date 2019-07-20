class Node(object):

    def __init__(self, item=None, next_item=None):
        self.item = item
        self.next_item = next_item

    def set_next(self, next_item):
        self.next_item = next_item

    def get_next(self):
        return self.next_item

    def get_item(self):
        return self.item


class MyStack(object):

    def __init__(self):
        self.top = None

    def push(self, item):
        t = Node(item)
        t.set_next(self.top)
        self.top = t

    def pop(self):
        if self.top:
            item = self.top.get_item()
            self.top = self.top.get_next()
            return item
        else:
            raise ValueError('Empty stacks')

    def peek(self):
        if self.top:
            return self.top.get_item()
        else:
            raise ValueError('Empty stacks')

    def is_empty(self):
        if self.top is None:
            return True


class MyQueue(object):

    def __init__(self):
        self.first = None
        self.last = None

    def add(self, item):
        t = Node(item)
        if self.last:
            self.last.set_next(t)
        self.last = t
        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first is None:
            raise ValueError('Queue is empty')
        t = self.first.get_item()
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return t

    def peek(self):
        if self.first is None:
            raise ValueError('Queue is empty')
        return self.first.get_item()


if __name__ == '__main__':
    my_stack = MyStack()
    for i in range(10):
        my_stack.push(i)
    print(my_stack.peek())
    my_stack.pop()
    print(my_stack.peek())