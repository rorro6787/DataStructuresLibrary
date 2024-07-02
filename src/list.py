class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        elements = [self.data]
        current = self.next
        while current is not None:
            elements.append(current.data)
            current = current.next
        return str(elements)

class List:
    def __init__(self, data=None):
        if isinstance(data, List):
            self.head = data.head
            self.length = data.length
            self.type = data.type
        elif data is None:
            self.head = None
            self.type = None
            self.length = 0
        else:
            self.__create_head(data)
    
    def append(self, element):
        if self.head is None:
            self.__create_head(element)
        elif type(element) != self.type:
            raise ValueError(f'List type {self.type} different than element type {type(element)}...')
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(element)
            self.length += 1 
    
    def delete(self, element, all=False):
        if self.head is None:
            raise IndexError("Cannot delete from an empty list")
        elif type(element) != self.type:
            raise ValueError(f'List type {self.type} different than element type {type(element)}...')
        else:
            iteraciones = 1
            while iteraciones == 1 or (all and self.contains(element)):
                iteraciones -= 1
                previous = None
                current = self.head
                while current and current.data != element:
                    previous = current
                    current = current.next
                if not current:
                    if not all:
                        raise ValueError("Element not found in the list")
                elif previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

    def contains(self, element):
        try:
            self.find(element)
            return True
        except ValueError:
            return False
    
    def find(self, element, which=1):
        if which < 1:
            raise IndexError(f'Cannot find an element repeated {which} times')
        if self.head is None:
            raise IndexError("Cannot find from an empty list")
        elif type(element) != self.type:
            raise ValueError(f'List type {self.type} different than element type {type(element)}...')
        else:
            current = self.head
            pos = 1
            while current:
                if current.data == element:
                    if which == 1:
                        return pos
                    which -= 1
                current = current.next
                pos += 1
            raise ValueError(f'Element {element} not found in the list')

    def isEmpty(self):
        return self.length == 0

    def __create_head(self, element):
        self.head = Node(element)
        self.type = type(element)
        self.length = 1
    
    def __str__(self):
        if not self.head:
            return f'Empty List'
        else:
            return f'List type {self.type} with {self.length} elements = {str(self.head)}'

def main():
    lista = List()
    print(lista)
    lista.append(5)
    print(lista)
    lista.append(6)
    lista.append(5)
    lista.append(6)
    print(lista)
    print(lista.find(6, which=2))
    lista.delete(2, all=True)
    print(lista)
    
if __name__ == "__main__":
    main()