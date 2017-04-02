import pprint
import math
pp = pprint.PrettyPrinter(indent=4)
from array import array
dim=rows=cols=4

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
		
    def search(self, node, data):
        """
        # Search function will search a node into tree.
        # """
        #if root is None or root is the search data.
        if node.data == data:
            return node

        if node.right!=None:
            return self.search(node.right, data)
        elif node.left!=None:
            return self.search(node.left, data)
        elif node.middle1!=None:
            return self.search(node.middle1, data)			
        elif node.middle2!=None:
            return self.search(node.middle2, data)
      
    
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
            
            print(space,q)
            #print (" ")
            self.traversePreorder(root.left,pos-2)
            self.traversePreorder(root.right,pos-1)
            self.traversePreorder(root.middle1,pos)
            self.traversePreorder(root.middle2,pos+1)        
###################################################################
tree=Tree()
def linearverticalconflict(mat):
	puzz=eval(mat)
	lc=0
	for row in range(4):
		max=-1
		for col in range(4):
			cellvalue=puzz[row][col]
			if cellvalue !=0 and (cellvalue-1)/dim == row:
				if cellvalue>max:
					max=cellvalue
				else: #linear conflict, one tile must move up or down to allow the other to pass by and then back up
						#add two moves to the manhattan distance
					lc +=2
	return lc					
	
def linearhorizontalconflict(mat):
	puzz=eval(mat)
	lc=0
	for col in range(4):
		max=-1
		for row in range(4):
			cellvalue=puzz[row][col]
			if cellvalue !=0 and cellvalue%dim == col+1:
				if cellvalue>max:
					max=cellvalue
				else:   
				#linear conflict, one tile must move left or right to allow the other to pass by and then back up
						#add two moves to the manhattan distance
					lc +=2
	
	return lc

def linearconflict(puzz):
	h=distance(puzz)
	        #Two tiles tj and tk are in a linear conflict if tj and tk are in the same line, the goal positions of tj and tk are both in that line,
	          # tj is to the right of tk and goal position of tj is to the left of the goal position of tk
	h += linearverticalconflict(puzz)
	h += linearhorizontalconflict(puzz)
	return h  
  
def isSolvable(mat):
    puzzle=eval(mat)
    parity=0
    gridwidth=len(puzzle)
    puzz=[]
	
    for x in puzzle:
        for elt in x:
            puzz.append(elt)
            #print(puzz)			
    print ('gridwidth') 
    #print(puzz[8])
    row=0
    blankrow=0
    for i in range(0,len(puzz)):
        j=i+1
        if i % gridwidth == 0:
            row+=1
        if puzz[i]==0:
            blankrow=row
            print ('blank %d'% blankrow)
            continue 
        for j in range(i+1,len(puzz)):
             if puzz[i]>puzz[j] and puzz[j]!=0:
                 parity+=1
        print ('parity %d'% parity)

    if gridwidth % 2 == 0: 
        if blankrow % 2 == 0: 
            return parity % 2 != 0;
        else: 
            return parity % 2 == 0;
        
    else: 
        return parity % 2 == 0;
		
def A_star(puzz,goal,root):
   
    front = [[distance(puzz), puzz]] 
    expanded = []
    expanded_states=0
    while front:
        i = 0
        for j in range(1, len(front)):
            if front[i][0] > front[j][0]:
                i = j
        path = front[i]
        front = front[:i] + front[i+1:]
        endnode = path[-1]
        if endnode == goal:
            break
        if endnode in expanded: continue
        for k in moves(endnode,root):
            if k in expanded: continue
            newpath = [path[0] + distance(k) - distance(endnode)] + path[1:] + [k] 
            front.append(newpath)
            expanded.append(endnode)
        expanded_states += 1 
    print ("Expanded nodes:", 
	expanded_states)
    print ("Solution:")
    pp.pprint(path)


def moves(mat,root): 
   
    output = []  

    m = eval(mat)  
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); 

    if i > 0:                                   
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
      output.append(str(m))
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
      
    if i < 3:                                   
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
      output.append(str(m))
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:                                                      
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
      output.append(str(m))
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < 3:                                   
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
      output.append(str(m))
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
    #print(output)
    tree.insert(root,output)
    return output


def distance(mat):
     
    distance = 0
    puzz = eval(mat) 
    
    for i in range(rows):
        for j in range(cols):
	
            puzz[i][j]=int(puzz[i][j])
            if puzz[i][j] == 0 : continue
            distance += abs(i - puzz[i][j] / 4)
            distance +=abs(j -  (puzz[i][j]%4))
    return distance

	

	
if __name__ == '__main__':
    print  ("input the numbers from 0-15. ")                                                  
    print ("Note : press space-bar after entering each number to enter next one  ")
    numbers = [int(x) for x in input().split()]                                               
    puzzle = str([numbers[i:i+rows] for i in range(0, len(numbers), rows)])
    goal = str([[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15]])
    
    root=tree.root=None
    if isSolvable(puzzle) : 
        print ("solvable")	
        root=tree.insert(root, puzzle)
        tree.traversePreorder(root)
        print(char(x) for x in input())
        A_star(puzzle,goal,root)
        #tree.traversePreorder(root)
    else:
        print("not solvable") 