class TEYY:
    def __init__(self,TEY):
        self.data=TEY
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
root=TEYY("A")
root.left=TEYY("b")
root.right=TEYY("c")
root.left.left=TEYY("d")
root.left.right=TEYY("e")
print("INORDER")
inorder(root)
print("POSTORDER")
postorder(root) 
print("PREORDER")
preorder(root)