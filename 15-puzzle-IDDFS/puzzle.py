from collections import deque
import random
import Tree
import Queue
Tree.mtree=Tree.Tree()
m=Tree.mtree
rows=4
cols=4
nums = [0] + list(range(1, rows * cols)) 
goal = [nums[i:i+rows] for i in range(0, len(nums), rows)]
q=Queue.LifoQueue()


#/////////////////////////////////////////////////////////////////////////////
def isSolvable(mat):
    puzzle=mat
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
		
def get_moves(p,root):
	moves = []
	srow, scol = next((r, c)
		for r, l in enumerate(p)
			for c, v in enumerate(l) if v == 0)
		#print (srow)
	def swap(row, col):
		import copy
		s = copy.deepcopy(p)
		s[srow][scol], s[row][col] = s[row][col], s[srow][scol]
		
		print (s)
		#m.insert(root, s)
		return s

			#up
	if srow > 0:
		moves.append(swap(srow - 1, scol))
			# left
	if scol < cols - 1:
		moves.append(swap(srow, scol + 1))
		# down
	if srow < rows - 1:
		moves.append(swap(srow + 1, scol))
		# right
	if scol > 0:
		moves.append(swap(srow, scol - 1))
	   
	
	return moves


def IDDFS(p, g,root):
    import itertools

    def dfs(routeQueue, depth):
        if depth == 0:
            return
        if routeQueue[-1] == g:
            return routeQueue
        for move in get_moves(routeQueue[-1],root):
            if move not in routeQueue:
                next_routeQueue = dfs(routeQueue + [move], depth - 1)
                if next_routeQueue:
                    return next_routeQueue
                
    for depth in itertools.count():          #to limit the depth 
        routeQueue = dfs([root.data], depth)
        if routeQueue:     
            return routeQueue    		   

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////	 
def main():
    
    rows=4
    cols=4
    Tree.root=None
    
    root=Tree.root
    #print  ("input the numbers from 0-15. ")                                                  #   ISSUE1 : you can input the numbers but my tree is creating nodes using 
    print ("Note : press spacebar after entering each number to enter next one  ")            #  recursion method and if steps of solving puzzle increase 15-20 ,
    numbers = [int(x) for x in input().split()]                                               #  the recursion limit exceed 
    #print (numbers)                                                                           # ISSUE NO MORE 
    #numbers = [1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    
    puzzle=[numbers[i:i+rows] for i in range(0, len(numbers), rows)]
    #numbers = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1]	
    #goal=[numbers[i:i+rows] for i in range(0, len(numbers), rows)]	
    print ("Initial problem :")
    print(" ")
    for elt in puzzle:
        print(elt)
    if isSolvable(puzzle) :
        print(" Goal state Reachable")
        print(char(x) for x in input())
    else:
        print(" Goal state UnReachable")
        exit()
        retutn
    root=m.insert(root, puzzle)
        
    
    r=IDDFS(puzzle,goal,root)
    print(" ")    
    print ("Tree of possible moves :")		
    #m.traversePreorder(root)
    print ("Route of goal is :")
    print(" ")	
    for elt in r:
        for t in elt:
            print ("          ",t)
        print (" ")
    print(" ")		
    print("The lenth of solution is :" , len(r))
if __name__ == "__main__":
    main()		