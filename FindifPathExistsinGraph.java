class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (edges.length == 1)
            return true;
        
        Map<Integer, List<Integer>> edge = new HashMap<>();
        for(int i = 0; i < edges.length; i ++){
            int a = edges[i][0];
            int b = edges[i][1];
            edge.computeIfAbsent(a, k -> new ArrayList<>()).add(b); // make the array list if the given key does not exist
            edge.computeIfAbsent(b, k -> new ArrayList<>()).add(a);
        }

        Set<Integer> visited = new HashSet<>();
        visited.add(source);
        Stack<Integer> s = new Stack<>();
        s.push(source);

        while (s.size() > 0){
            int node = s.pop();
            if (node == destination){
                return true;
            }
            for (int neiNodes: edge.get(node)){
                if (!visited.contains(neiNodes)){
                    visited.add(neiNodes);
                    s.push(neiNodes);
                }
            }
        }
        return false;
    }

    // Time: O(N + Edges)
    // Space: O(N + Edges)
    // N number of nodes, Edges number of edges
}
