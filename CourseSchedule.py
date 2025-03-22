class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        direc = defaultdict(list)
        for a, b in prerequisites:
            direc[a].append(b)

        graph = [0] * numCourses

        def dfs(i):
            if graph[i] == 1: return False 
            elif graph[i] == 2: return True 

            graph[i] = 1 #Being visited

            for nodes in direc[i]: #if direc[i] doesn't exist, it will just return []
                if not dfs(nodes):
                    return False

            graph[i] = 2 #Already visited
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    #Time: O(N + E) number of nodes + edges
    #Space: O(N + E)
