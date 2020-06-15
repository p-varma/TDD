#############################################################################

# using built in function
from binarytree import build

def build_binary(items):
    print("Using built in module to create binary tree")
    btree = build(items)
    print(btree)
    return btree


def inorder(btree):
    print('Using built in module to do inorder print')
    print(btree.inorder)

def postorder(btree):
    print('Using built in module to do postorder print')
    print(btree.postorder)

def preorder(btree):
    print('Using built in module to do preorder print')
    print(btree.preorder)



#############################################################################

class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

def insert_level_order(arr,root,i,n):
    #base case for recursion
    if i< n:
        temp = Node(arr[i])
        root = temp

        # insert left childjmm
        root.left = insert_level_order(arr,root.left, 2*i+1, n)
        # insert right child
        root.right = insert_level_order(arr,root.right,2*i +2, n)
    return root

def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)
        # then print the data of node
        print(root.val)
        # now recur on right child
        printInorder(root.right)
###############################################################################

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    btree = build_binary(arr)
    inorder(btree)
    preorder(btree)
    postorder(btree)
    n = len(arr)
    root = None
    root = insert_level_order(arr,root,0,n)
    printInorder(root)

