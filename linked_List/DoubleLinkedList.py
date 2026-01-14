

class Student :
    def __init__(self ) :
        self._id = None
        self._name = None
        self._grades = None
    def set_Id (self , id : int) :
        self._id = id
    def set_Name (self , name : str) :
        self._name = name
    def set_Grades (self , grades : list) :
        self._grades = grades
    def get_id (self) :
        return self._id
    def get_name (self) :
        return self._name
    def get_grades (self) :
        return self._grades
    def grade_average (self) :
        return sum(self._grades) / len(self._grades)






class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Double_Linked_List :
    def __init__(self ) :
        self.head = None
        self.tail = None
    def append (self , data ):
        node = Node(data)

        if self.head == None :
            self.head = node
            self.tail = node
        else :
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    def prepend (self , data ):
        node = Node(data)
        if self.head == None :
            self.head = node
            self.tail = node
        else :
            self.head.prev = node
            node.next = self.head
            self.head = node
    def delete_by_id (self , id : int) :
        deleted = False
        temp = self.head
        while temp:
            if temp.data.get_id() == id :
                deleted = True
                if temp == self.head :
                    if self.head == self.tail :
                        self.head = None
                        self.tail = None
                    else :
                        self.head = temp.next
                        self.head.prev = None
                elif temp == self.tail :
                    self.tail = temp.prev
                    self.tail.next = None
            else :
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
            temp = temp.next
        return deleted
    def search_by_name (self , name) :
        current = self.head
        found = False
        listNames = []
        while current :
            if current.data.get_name() == name :
                found = True
                listNames.append(current.data)
            current = current.next

        if found == False :
            return None
        else :
            return listNames
    def search_by_id (self , id : int) :
        current = self.head
        while current :
            if current.data.get_id() == id :
                return current
            current = current.next
        return False
    def count_nodes(self):
        counter = 0
        current = self.head
        while current :
            counter += 1
            current = current.next
        return counter
    def display_forward (self) :
        print("Forward")
        current = self.head
        while current :
            print(current.data.get_name() , current.data.get_id() , current.data.get_grades() , current.data.grade_average())
            current = current.next
    def display_backward (self) :
        current = self.tail
        while current :
            print(current.data.get_name() , current.data.get_id() , current.data.get_grades() , current.data.grade_average())
            current = current.prev







