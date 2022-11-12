'''
PROBLEM: 

Write a function in python that can reverse a string using stack data structure. 
Use [Stack class]
    ```
    reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
    ```
'''

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

    
    def reverse_string(self, txt):
        print("pushing data.")
        for i in txt:
            self.push(i)
        reverse_str = str()
        print("pop data")
        for i in range(self.top + 1):
            reverse_str += self.pop()
        
        return reverse_str

    
    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    stack = Stack()
    reverse_str = stack.reverse_string("We will conquere COVID-19")
    print(reverse_str)
    expected_result = "91-DIVOC ereuqnoc lliw eW"
    print(reverse_str == expected_result)
    print(stack)
    