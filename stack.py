class Stack:
    def __init__(self,length=10):
        self.stack=[]
        self.maxlength=length
        print(f"Stack created of max size {self.maxlength}")

    def push(self,element):
        if self.length()>=self.maxlength:
            raise Exception("Overflow")
        else:
            self.stack.append(element)
            return  self.stack

    def Pop(self):
        if self.length() > 0:
            return self.stack.pop()
        else:
            raise Exception("Underflow")
    def length(self):
        return len(self.stack)


if __name__=='__main__':
    stack1 = Stack()
    print(stack1.push(5))
    print(stack1.push(8))
    print(stack1.push(40))
    print(stack1.push(34))
    print(stack1.Pop())
    print(stack1.length())



