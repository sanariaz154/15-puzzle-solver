class Node:
    """
    Class Node
    """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.middle1 = None
        self.right = None
        self.middle2=None
		
		
class Tree:
    """
    Class tree will provide a tree as well as utility functions.
    """

    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node , data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if node.data==data:
            return node
        elif node.left==None:
            node.left = self.insert(node.left, data)
        elif node.right==None:
            node.right = self.insert(node.right, data)
        elif node.middle1==None:
            node.middle1 = self.insert(node.middle1, data)	
        else:
            node.middle2 = self.insert(node.middle2, data)

        return node


    
    # def traversePreorder(self, root):
        # """
        # traverse function will print all the node in the tree.
        # """
        # if root is not None:
            # # # iterate over deque's elements
            
            # q=root.data
            # for elt in q:
                # print(elt)
            # print (" ")
            # self.traversePreorder(root.left)
            # self.traversePreorder(root.right)
            # self.traversePreorder(root.middle1)
            # self.traversePreorder(root.middle2)
    def traversePreorder(self, root,pos=5):
        # """
        # traverse function will print all the node in the tree.
        # """
        if root is not None:
            # # iterate over deque's elements
            space=" "
            #pos=int(pos/2)
            # for i in range(0,pos):
                # space+=space
            q=root.data
            for elt in q:
                print(space,elt)
            #print (" ")
            self.traversePreorder(root.left,pos-2)
            self.traversePreorder(root.right,pos-1)
            self.traversePreorder(root.middle1,pos)
            self.traversePreorder(root.middle2,pos+1)        
    
