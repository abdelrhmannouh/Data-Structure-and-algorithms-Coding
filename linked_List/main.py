from DoubleLinkedList import Double_Linked_List
from DoubleLinkedList import Student

def main():
    s1 = Student()
    s1.set_Id(1)
    s1.set_Name("Ahmed")
    s1.set_Grades([1,2,3,4,5,6])
    s2 = Student()
    s2.set_Id(2)
    s2.set_Name("Mohammed")
    s2.set_Grades([1,2,3,4,5,6])
    s3 = Student()
    s3.set_Id(3)
    s3.set_Name("Ibrahim")
    s3.set_Grades([1,2,3,4,5,6])
    linked = Double_Linked_List()
    linked.append(s1)
    linked.append(s2)
    linked.append(s3)
    linked.display_forward()
    linked.display_backward()
if __name__ == "__main__":
    main()

