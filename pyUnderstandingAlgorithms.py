import networkx as nx

# The Depth-First-Search algorithm is a method for traversing a tree or graph.
# The Graph G is traversed starting from vertex v.
# https://en.wikipedia.org/wiki/Depth-first_search
def DFS(G, v):
    stack = []
    discovered = []
    stack.append(v)
    while len(stack)>0:
        u = stack.pop()
        if not u in discovered:
            discovered.append(u)
            for neighbor in G.neighbors(u):
                stack.append(neighbor)
    return discovered

# Use libraries if possible
G = nx.Graph()
G.add_nodes_from([0,1,2,3,4,5])
G.add_nodes_from([0,1,2,3])
G.add_nodes_from([1,4,5])
print(DFS(G, 0))


# I had problems with this file

Found a solution: pip install networkx (have to install wiht pip to make it available like npm)

Solution
O(m*n)

Explanation
Surprisingly, the runtime complexity is O(m*n). The
reason is that the main loop takes m iterations because each neighbor is
put into the stack and there are O(m) neighbors.
In each iteration, we check whether the current vertex
u is in the discovered list. Checking whether an element is in a list has
linear runtime complexity in the size of the list - n. Note that
this could be improved by using a (hash) set with constant complexity for
checking whether an element is in the set.