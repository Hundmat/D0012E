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
    def __init__(self, root, c):
        self.root   = root 
        self.c      = c   

        if c <= 0.5 or c >= 1:
            raise Exception("c must be between 0.5 and 1")

    def reorder(self,node):

        
        
        
        print2D(self.root)

        if node.left and node.left.right:
            self.rotateLeft(node.left)
        elif node.right and node.right.left:
            self.rotateRight(node.right)
        elif node.left and node.left.left:
            self.rotateRight(node)
        elif node.right and node.right.right:
            self.rotateLeft(node)
        else:
            sortedList=self.inorder(self.root,[])
            print(sortedList)
            self.root=Node(sortedList[len(sortedList)//2])
            
            for i in range(len(sortedList)//2-1, -1,-1):
                self.insert(sortedList[i])
                self.insert(sortedList[(len(sortedList)//2)+1+(len(sortedList)//2-1)-i])
    
    def inorder(self,root,res):
        if root:
 
            # First recur on left child
            self.inorder(root.left,res)
    
            # then print the data of node
            res += [root.val]
    
            # now recur on right child
            self.inorder(root.right,res)
            return res
    

    def rotateLeft(self, node):
        if node.right:
            node.right.parent   = node.parent
            if node.parent:
                if node.isRight():
                    node.parent.right   = node.right
                else:
                    node.parent.left    = node.right
            else:
                self.root   = node.right

            node.parent = node.right
            node.right  = node.right.left

            if node.right:
                node.right.parent = node

            node.parent.left    = node

    
    def rotateRight(self, node):
        if node.left:
            node.left.parent    = node.parent
            if node.parent:
                if node.isRight():
                    node.parent.right   = node.left
                else:
                    node.parent.left    = node.left
            else:
                self.root   = node.left

            node.parent = node.left
            node.left   = node.left.right

            if node.left:
                node.left.parent = node

            node.parent.right   = node


    def traverse(self,node):


        leftSize        = self.checker(self.root.left)
        rightSize       = self.checker(self.root.right)
        combinedSize    = leftSize + rightSize + 1

        balanced        = (
            (rightSize <= self.c * combinedSize) and
            (leftSize <= self.c * combinedSize)
        )

        if not balanced:
            self.reorder(node.parent)

    def checker(self, node):
        if node == None:
            return 0
        return self.checker(node.left) + self.checker(node.right) + 1


    def insert(self, value):                  # insert node
        node    = Node(value)    
        tree    = self.root
        while(True):                          # Loopar ignom fram tills den hittar sista noden i linked list
            if(node.val < tree.val):            # Kollar om den activa noden är större än tidigare node
                if (tree.left == None):      # Om det är sista noden så sätts den aktiva noden in efter på vänster sida
                    tree.left   = node
                    node.parent = tree
                    break
                else:                         # om inte så byts starnoden till nästa node i listan och sen görs samma koll
                    tree = tree.left
            else:
                if (tree.right == None):      # Kollar samma sak här men bara om den aktiva noden är större än start noden
                    tree.right      = node
                    node.parent     = tree
                    break
                else:
                    tree = tree.right
        self.traverse(node)
        print2D(self.root)
    
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
tree = BST(Node(10), 0.51)
tree.insert(11)
tree.insert(12)
# tree.insert(10)
tree.insert(13)
# tree.insert(12)
tree.insert(14)
tree.insert(15)

tree.insert(18)
# tree.insert(24)


print2D(tree.root)