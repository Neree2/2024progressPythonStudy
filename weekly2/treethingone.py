
class Node:
    def __init__(self,data) :
        self.left=None #the left side in pic thing
        self.right=None
        self.data=data
    def insert(self,data):
        # create a tree
        if self.data is None:
            self.data = data
        # check whether they already have datain or not
        else:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)

def inOrderPrint(r):
    if r is None:
        return
    else:   
        inOrderPrint(r.left)
        print(r.data)
        inOrderPrint(r.right)

if __name__=='__main__':
    print('My tree')
    root = Node('g')
    root.insert('c') 
    root.insert('b')  
    root.insert('a')
    root.insert('e') 
    root.insert('i')
    root.insert('h')
    root.insert('j')   

inOrderPrint(root)            