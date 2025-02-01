class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        
        # create a dictionary where the value is a list
        graph = defaultdict(list) # looks like this: {a: [b, c], b: [a]}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)        
        
        visited = set()
        visited.add(source)
        stack = [source]

        while stack: # Iterating the stack will perform DFS
            n = stack.pop()
            if n == destination:
                return True
            for node in graph[n]:
                if node not in visited:
                    visited.add(node)
                    stack.append(node) 
        return False

        # DFS using stack
        # Time: O(n + E)
        # Space: O(n + E)
        # nodes(n) from stack and Edges(E) from the graph (ie. deafaultdict(list))
