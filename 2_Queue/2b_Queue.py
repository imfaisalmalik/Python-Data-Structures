'''
PROBLEM:

TODO: Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main 
tutorial.
Binary sequence should look like,
```
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
```
Hint: Notice a pattern above. After `1`, the 2nd and 3rd number is 1+0 and 1+1. 
4th and 5th number are 2nd number (i.e. 10) + 0 and 2nd number (i.e. 10) + 1.
'''

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

def print_binary(limit=10):
    que = Que()
    count = 1
    binary = ['1']
    que.enque(binary[0])
    while count < limit:
        deque = que.deque()
        new_num1 = deque + '0'; que.enque(new_num1); binary.append(new_num1)
        new_num2 = deque + '1'; que.enque(new_num2); binary.append(new_num2)

        count += 2
    
    return binary[:limit]



if __name__ =="__main__":
    print(print_binary())
