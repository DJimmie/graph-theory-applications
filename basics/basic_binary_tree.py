class BinaryTree:
    def __init__(self,nodeData, left=None,right=None):
        self.nodeData=nodeData
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.nodeData)


tree=BinaryTree('FAILED HEAT')