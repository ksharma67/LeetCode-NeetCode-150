class DisjointSet:
    #constructor
    def __init__(self, n):
        self.reps = [i+1 for i in range(n)]
        self.ranks = [0 for i in range(n)]
    
    #find operation
    def find(self, e):
        #base case
        if(self.reps[e-1] == e):
            return e
        #otherwise, recursively find the representative of its parent!
        parent = self.reps[e-1]
        #for each element we find along path from e to rep, we will also record for intermediary nodes
        #path compression!
        self.reps[parent-1] = self.find(parent)
        return self.reps[parent-1]
    
    #union operation
    def union(self, e1, e2):
        #first, find two rep elements for the two elements e1 and e2!
        e1_rep = self.find(e1)
        e2_rep = self.find(e2)
        
        #check if two elements are part of same set!
        if(e1_rep == e2_rep):
            return
        #otherwise, compare the two ranks of two reps
        if(self.ranks[e1_rep-1] == self.ranks[e2_rep-1]):
            self.reps[e1_rep-1] = e2_rep
            self.ranks[e2_rep-1] += 1
        elif(self.ranks[e1_rep-1] < self.ranks[e2_rep-1]):
            self.reps[e1_rep-1] = e2_rep
        else:
            self.reps[e2_rep-1] = e1_rep


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #approach: use the union find data structure!
        #process each edge one by one!
        #if the two end nodes of the current edge belongs in same disjoint set, this implies
        #that current edge would be introduce a cycle and hence should be removed so we end up with tree
        #with n nodes!
        #we still have to traverse through the entire edges input array for possibility of multiple edges
        #than can introduce a cycle!
        #len(edges)  = num_nodes!
        
        #Time: O(n + nlgn) -> O(nlgn)
        #Space: O(2n) -> O(n)
        #in worst case, we do n-1 calls to union! union operation takes logn time!(unionization by rank)
        
        answer = None
        uf = DisjointSet(len(edges))
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            #check if two nodes are part of same set! -> Edge that introduces a cycle
            if(uf.find(node1) == uf.find(node2)):
                answer = edge
                continue
            #otherwise, merge two disjoint sets or connected components into one overall connected
            #component!
            else:
                uf.union(node1, node2)
        return answer
