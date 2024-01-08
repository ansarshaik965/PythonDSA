import array

class Stack:
    def __init__(self):
        self.my_array=array.array('i',[])
    def is_empty(self):
        if len(self.my_array):
            return False
        else:
            return True
    def push(self,element):
        self.my_array.append(element)
    def pop(self):
        if self.is_empty():
            print("stack is empty can't pop")
        else:
            self.my_array.pop()

if __name__=="__main__":
    stack=Stack()
    print(stack.my_array)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.my_array)

    stack.pop()
    print(stack.my_array)
    stack.pop()
    print(stack.my_array)
    stack.pop()
    print(stack.my_array)
    stack.pop()