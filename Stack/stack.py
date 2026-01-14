from linked_List.DoubleLinkedList import Student
class Node :
    def __init__ (self, data) :
        self.data = data
        self.next = None
class Stack :
    def __init__ (self) :
        self.tos = None
    def push(self , data) :
        node  = Node(data)
        if self.is_empty() :
            self.tos = node
        else :
            node.next = self.tos
            self.tos = node
    def pop (self) :
        if self.is_empty() :
            return None
        else :
            s = self.tos.data
            self.tos = self.tos.next
            return s
    def is_empty(self) :
        if self.tos == None :
            return True
        else :
            return False
    def peek(self) :
        if self.is_empty() :
            return None
        else :
            return self.tos.data
    def size(self) :

        if self.is_empty() :
            return 0
        else :
            count = 0
            current = self.tos
            while current :
                count += 1
                current = current.next
            return count


if __name__ == '__main__':
    print("stack")