from stack import Stack
from linked_List.DoubleLinkedList import Student



def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    s = Student()
    s.set_Id(5)
    s.set_Name("Ahmed")
    stack.push(s)
    print (stack.peek())
    print (stack.pop())
    print (stack.is_empty())
    print (stack.size())