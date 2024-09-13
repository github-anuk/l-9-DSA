class TEWE:
    def __init__(self,te):
        self.data=te
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
root=TEWE(1)
root.left=TEWE(2)
root.right=TEWE(3)
root.left.left=TEWE(4)
root.left.right=TEWE(5)
root.right.left=TEWE(6)
root.right.right=TEWE(7)
to=int(input("Enter which kind of transversal you want {option 1 -- inorder , option 2 -- postorder , option 3 -- preorder}"))
if to ==1:
    inorder(root)
elif to==2:
    postorder(root)
elif to==3:
    preorder(root)
else:
    print("error no such thing exists")

