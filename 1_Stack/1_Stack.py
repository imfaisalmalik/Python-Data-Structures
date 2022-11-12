class Stack:
    def __init__(self):
        self.top = -1
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.top > -1:
            data = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1
            return data
        else:
            print("Stack is empty.")

    def peek(self):
        return self.stack[self.top]
    
    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    stack = Stack()
    numbers = [5,15,25,35,45,55, 25, 65]

    for num in numbers:
        stack.push(num)
    
    print(f"Stack: {stack}")

    print(f"Peek: {stack.peek()}")

    for i in range(11):
        print(f"Pop: {stack.pop()}")