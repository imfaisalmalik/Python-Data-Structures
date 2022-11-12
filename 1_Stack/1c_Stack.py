''' TODO : Write a function in python that checks if paranthesis in the string are balanced or not. 
Possible parantheses are "{}',"()" or "[]". Use Stack.  
    ```
    is_balanced("({a+b})")     --> True
    is_balanced("))((a+b}{")   --> False
    is_balanced("((a+b))")     --> True
    is_balanced("))")          --> False
    is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
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
    
    def match_paranthesis(self, ch1, ch2):
        paranthesis = {
            "}": "{",
            ")":"(", 
            "]":"["
        }
        return paranthesis[ch1] == ch2

    def is_balanced(self, txt):
        print(txt, end=" >> ")
        for ch in txt:
            # print(ch, end=", ")

            if ch in ["{" , "[" , "("]:
                # print(f"detected character: {ch}")
                self.push(ch)
                # print(f"pushed: {self.stack}")
            if ch in ["}" , "]" , ")"]:
                if self.top == -1:
                    return False 
                elif not self.match_paranthesis(ch, self.pop()):
                    return False
            # print(f"self.top >> {self.top}")
        return self.top == -1
        
    
    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_balanced("({a+b})"))
    print(stack.is_balanced("))((a+b}{"))
    print(stack.is_balanced("((a+b))"))
    print(stack.is_balanced("((a+g))"))
    print(stack.is_balanced("))(("))
    print(stack.is_balanced("[a+b]*(x+2y)*{gg+kk}"))

'''
LOGIC >> Only push the starting paranthesis 
Upon getting the ending paranthesis, pop the data and match.

LIFO >> Paranthesis, e.g., ``(, {, [`` Last In >> First out ``], }, )``

'''