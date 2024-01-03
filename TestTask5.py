class Node:
    def __init__(self, element):
        self.element = element
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if not self.tail:
            return None
        element = self.tail.element
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return element

    def shift(self):
        if not self.head:
            return None
        element = self.head.element
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return element

    def unshift(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

d_list = DoublyLinkedList()
d_list.push(1)
d_list.push(2)
d_list.push(3)

print("Двусвязный список:")
current_node = d_list.head
while current_node is not None:
    print(current_node.element)
    current_node = current_node.next

print("\nПоследний элемент:", d_list.pop())
print("Первый элемент:", d_list.shift())

print("\nСписок после удаления элементов:")
current_node = d_list.head
while current_node is not None:
    print(current_node.element)
    current_node = current_node.next

d_list.unshift(5)
print("\nСписок после добавления элемента в начало:")
current_node = d_list.head
while current_node is not None:
    print(current_node.element)
    current_node = current_node.next