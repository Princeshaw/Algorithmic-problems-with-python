class Node:
    def __init__(self,data,parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root is None:
            self.root = Node(data,None)
        else:
            self.insert_node(data,self.root)
    def insert_node(self,data,node):
        if data<node.data:
            if node.leftChild:
                self.insert_node(data,node.leftChild)
            else:
                node.leftChild = Node(data,node)
        if data>node.data:
            if node.rightChild:
                self.insert_node(data,node.rightChild)
            else:
                node.rightChild = Node(data,node)
    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)
    def traverse_in_order(self,node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)
        print("%s" %node.data)
        if node.rightChild:
            self.traverse_in_order(node.rightChild)
    def max(self):
        if self.root:
            return self.get_max(self.root)
    def get_max(self,node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        return(node.data)
    def min(self):
        if self.root:
            return self.get_min(self.root)
    def get_min(self,node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        return node.data
    def remove(self,data,node):
        if node is None:
            return
        if data<node.data:
            self.remove(data,node.leftChild)
        elif data>node.data:
            self.remove(data,node.rightChild)
        else:
            if node.leftChild is None and node.rightChild is None:
                print("removing single leaf----------- %d" %node.data)
                parent = node.parent
                if parent is not None and parent.leftChild == node:
                    parent.leftChild =None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild =None
                if parent is None:
                    self.root = None
                del node
            elif node.leftChild is None and node.rightChild is not None:
                print("removing a node with single child......")
                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                    else:
                        self.root =node.rightChild
                    node.rightChild.parent = node.parent
                    del node
            elif node.leftChild in None and node.rightChild is not None:
                print("removing a node with single child......")
                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                    else:
                        self.root =node.rightChild
                    node.rightChild.parent = node.parent
                    del node
            elif node.leftChild in None and node.rightChild is not None:
                print("removing a node with single child......")
                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.rightChild
                    if parent.rightChild == node:
                        parent.rightChild = node.rightChild
                    else:
                        self.root =node.rightChild
                    node.rightChild.parent = parent
                    del node
            elif node.rightChild in None and node.leftChild is not None:
                print("removing a node with single child......")
                parent = node.parent
                if parent is not None:
                    if parent.leftChild == node:
                        parent.leftChild = node.leftChild
                    if parent.rightChild == node:
                        parent.rightChild = node.leftChild
                    else:
                        self.root =node.leftChild
                    node.leftChild.parent = parent
                    del node
            else:
                print("removing node with two children")
                predecessor = self.get_predecessor(node.leftChild)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove(data,predecessor)
    def get_predecessor(self,node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        return node





bst = BinarySearchTree()
bst.insert(12)
bst.insert(8)
bst.insert(18)
bst.insert(0)
bst.insert(-1)
bst.insert(78)
bst.remove(18,bst.root)
bst.traverse()
print(bst.max())
print(bst.min())
bst.traverse()
