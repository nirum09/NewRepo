class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=',')
            temp=temp.next
        print('\n')

    def getlength(self):
        count,temp=0,self.head
        while(temp):
            count+=1
            temp=temp.next
        return count

    def insert(self,node,position):

        if not isinstance(node,Node) and position<0:
            print('Invalid node or position.')
            raise

        if position==0:
           node.next,self.head=self.head,node
        elif position>self.getlength():
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=node
        else:
            temp,count=self.head,0
            while(count<position-1):
                temp=temp.next
                count+=1
            temp.next,node.next=node,temp.next

    def delete(self,position):
        if position<0 or position>self.getlength():
            print('Invalid position for delete.')
            raise

        if position==0:
            self.head.next,self.head=None,self.head.next
        elif position==self.getlength():
            temp=self.head
            while(temp.next):
                second_last=temp
                temp=temp.next
            second_last.next=None
        else:
            temp,count=self.head,0
            while(count<position-2):
                temp=temp.next
                count+=1
            temp.next=temp.next.next
            temp.next.next=None



if __name__=='__main__':
    LL=LinkedList()
    LL.head=Node(8)
    second=Node(0)
    third=Node(3)
    fourth=Node(4)
    LL.head.next=second
    second.next=third
    third.next=fourth
    #Insert Node
    newnode=Node(10)
    LL.insert(newnode,10)
    LL.printlist()
    #Delete Node
    LL.delete(3)
    LL.printlist()
    print(f'Length of linkedlist:{LL.getlength()}')