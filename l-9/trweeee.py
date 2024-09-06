class Trwee:
    def __init__(self,t):
        self.data=t
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
def preorder(root):
    if root is None:
        return
    else:
        print(root.data)
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
root=Trwee(100)
root.left=Trwee(20)
root.right=Trwee(30)
root.left.left=Trwee(40)
root.left.right=Trwee(50)
root.right.left=Trwee(60)
root.right.right=Trwee(70)
root.left.left.left=Trwee(75)
root.left.left.right=Trwee(80)
root.left.right.left=Trwee(72)
root.left.right.right=Trwee(74)
print("INORDER TRAVERSAL")
inorder(root)
print("PREORDER TRAVERSAL")
preorder(root)
print("postoreder transversal")
postorder(root)