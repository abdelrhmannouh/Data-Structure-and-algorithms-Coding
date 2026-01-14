class Queue :
    def __init__(self , capacity = 0) :
        self.items =  [None]* capacity
        self.front = -1
        self.rear = -1

    def isEmpty(self) :
        if self.front == -1 :
            return True
        else :
            return False
    def enqueue(self , item) :
        if self.front == -1 :
            self.front = 0
        self.rear = self.rear + 1
        self.items[self.rear] = item
    def dequeue(self)  :
        if self.isEmpty() :
            raise IndexError("Queue is empty")
        else :
            dequeue = self.items[self.front]
            self.front = self.front + 1
            if self.front == self.rear :
                self.rear = self.rear - 1
            return dequeue
    def front(self) :
        if self.isEmpty() :
            return -1
        else :
            return self.front
    def size (self) :
        if self.isEmpty() :
            return 0
        else :
            return self.rear - self.front + 1
def main():
    queue = Queue(capacity= 10)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.isEmpty())
    print(queue.dequeue())
    print(queue.dequeue())
if __name__ == "__main__":
    main()




# we have not  Handled fall case yet


