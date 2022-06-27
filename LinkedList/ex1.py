class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'[{self.data}]->{self.next}'


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def length(self):
        counter = 0
        tmp = self.head
        while tmp:
            counter += 1
            tmp = tmp.next

        return counter


linked_list = LinkedList()
tmp = Node(1)
linked_list.head = tmp
for i in range(2, 5):
    tmp.next = Node(i)
    tmp = tmp.next

print(linked_list)
print(linked_list.length())