# 15-puzzle-solver
The 15-puzzle (also called Gem Puzzle, Game of Fifteen and many others) is a sliding puzzle that consists of a frame of numbered square tiles in random order with one tile missing. The puzzle also exists in other sizes, particularly the smaller 8-puzzle. 
 
 # Solvabilty of puzzle
  There is a method to check whether any given game state is solvable.
    ( (grid width odd) && (#inversions even) )  ||  ( (grid width even) && ((blank on odd row from bottom) == (#inversions even)) )
    
    The formula says:
    
         1. If the grid width is odd, then the number of inversions in a solvable situation is even.
         2. If the grid width is even, and the blank is on an even row counting from the bottom (second-last, fourth-last etc), then the   number of inversions in a solvable situation is odd.
         3. If the grid width is even, and the blank is on an odd row counting from the bottom (last, third-last, fifth-last etc) then the number of inversions in a solvable situation is even.

While , An inversion is when a tile precedes another tile with a lower number on it. The solution state has zero inversions.
for more information see https://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html

# Iterative Deepening Depth First Search Algorithm
Iterative deepening depth-first search (IDDFS) is an extension to the ‘vanilla’ depth-first search algorithm, with an added constraint on the total depth explored per iteration. This addition produces equivalent results to what can be achieved using breadth-first search, without suffering from the large memory costs. Due to BFS’s storage of fringe vertices in memory, Od^b memory space may be required (b = branching factor), this is a stark contrast to IDDFS’s O(bd) worst-case memory requirements.

# A-star searching Algorithm
A-star is an informed search algorithm, meaning that it solves problems by searching among all possible paths to the solution (goal) for the one that incurs the smallest cost (least distance travelled, shortest time, etc.), and among these paths it first considers the ones that appear to lead most quickly to the solution.
At each iteration of its main loop, A-star needs to determine which of its partial paths to expand into one or more longer paths. It does so based on an estimate of the cost (total weight) still to go to the goal node. Specifically, A-star selects the path that minimizes
{\displaystyle f(n)=g(n)+h(n)} f(n)=g(n)+h(n)

where n is the last node on the path, g(n) is the cost of the path from the start node to n, and h(n) is a heuristic that estimates the cost of the cheapest path from n to the goal.

   # Hueristic (Linear Conflict)
   The heuristic is problem-specific. For the algorithm to find the actual shortest path, the heuristic function must be admissible, meaning that it never overestimates the actual cost to get to the nearest goal node.
   
     # Linear Conflict Tiles Definition:
     Two tiles tj and tk are in a linear conflict if tj and tk are in the same line, the goal positions of tj and tk are both in that line, tj is to the right of tk and goal position of tj is to the left of the goal position of tk.

The linear conflict adds at least two moves to the Manhattan Distance of the two conflicting tiles, by forcing them to surround one another. Therefore the heuristic function will add a cost of 2 moves for each pair of conflicting tiles.

The Linar Conflict Heuristic is admissible.
    
