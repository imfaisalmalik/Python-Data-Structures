class Que:
    def __init__(self) -> None:
        self.size = 0
        self.que = []
    
    def enque(self, data):
        self.que.append(data)
        self.size += 1

    def deque(self):
        if self.size > 0:
            data  = self.que[0]
            del self.que[0]
            self.size -= 1
            return data
        else:
            print("Que is empty.")

    def peek(self):
        return self.que[0]

    def __str__(self):
        return str(self.que)


if __name__ =="__main__":
    que = Que()

    numbers = [5,15,25,35,45,55, 25, 65]

    for num in numbers:
        que.enque(num)
    
    print(f"Que: {que}")

    print(f"Peek: {que.peek()}")

    for i in range(11):
        print(f"Pop: {que.deque()}")
