class Node:
    def __init__(self, val):
        self.val        = val
        self.left       = None
        self.right      = None
        self.parent     = None
    
    def isRight(self):
        if self.parent == None:
            return False
        return self.parent.right == self

    def isLeft(self):
        if self.parent == None:
            return False
        return self.parent.left == self

class BST:
    def __init__(self, root):
        self.root  = root 

    def reorder(self, node):
        print("reorder", node.val)

        if node.isRight() and node.parent.isLeft():
                self.rotateLeft(node)
                self.rotateRight(node)
        elif node.isLeft() and node.parent.isRight():
                self.rotateRight(node)
                self.rotateLeft(node)
        elif node.isRight() and node.parent.isRight():
                self.rotateLeft(node.parent)
        elif node.isLeft() and node.parent.isLeft():
                self.rotateRight(node.parent)

    def rotateLeft(self, node):
        print("rotateLeft", node.val)
        parent              = node.parent
        grandParent         = parent.parent
        if grandParent == None:
            self.root       = node
        node.parent         = grandParent
        parent.right        = node.left
        node.left           = parent
        parent.parent       = node

    def rotateRight(self, node):
        print("rotateRight", node.val)
        parent              = node.parent
        grandParent         = parent.parent
        if grandParent == None:
            self.root       = node
        node.parent         = grandParent
        parent.left         = node.right
        node.right          = parent
        parent.parent       = node

    def traverse(self, node):

        parent          = node.parent
       
        if parent:
            leftSize      = self.checker(parent.left)
            rightSize     = self.checker(parent.right)
            combinedSize  = leftSize + rightSize +1
            
            print(node.val, leftSize, rightSize, combinedSize, rightSize <= 0.500001 * combinedSize,
                (leftSize <= 0.500001 * combinedSize))

            balanced        = (
                (rightSize <= 0.6 * combinedSize) and
                (leftSize <= 0.6 * combinedSize )
            )
            LorR=self.checkLorR(node)
            if balanced:
                self.traverse(parent)
            else:
                self.reorder(LorR)          

    def checker(self, node):
        if node == None:
            return 0
        return self.checker(node.left) + self.checker(node.right) + 1

    def checkLorR(self,node):
        if( node.right == None and node.left == None):
            return None
        elif node.right==None:
            return node.left
        else:
            return node.right


    def insert(self, value):                  # insert node
        node    = Node(value)    
        tree    = self.root
        while(True):                          # Loopar ignom fram tills den hittar sista noden i linked list
            if(node.val < tree.val):            # Kollar om den activa noden är större än tidigare node
                if (tree.left == None):      # Om det är sista noden så sätts den aktiva noden in efter på vänster sida
                    tree.left   = node
                    node.parent = tree
                    print2D(self.root)
                    self.traverse(node)
                    break
                else:                         # om inte så byts starnoden till nästa node i listan och sen görs samma koll
                    tree = tree.left
            else:
                if (tree.right == None):      # Kollar samma sak här men bara om den aktiva noden är större än start noden
                    tree.right      = node
                    node.parent     = tree
                    print2D(self.root)
                    self.traverse(node)
                    break
                else:
                    tree = tree.right
    
COUNT = [10]
def print2DUtil(root, space):

    # Base case
    if (root == None):
        return
    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
# count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    # Process left child
    print2DUtil(root.left, space)

def print2D(root):
    print2DUtil(root, 0)
    print("\n====================\n")



#arr =[11,3,7,9,12,43,4,1,10,85]
tree = BST(Node(11))
tree.insert(4)
tree.insert(3)
tree.insert(15)
tree.insert(16)
#tree.insert(12)
#tree.insert(14)
# tree.insert(15)
# tree.insert(16)

print2D(tree.root)