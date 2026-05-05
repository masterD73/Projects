# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------

from collections import deque


# Function to check if the graph is Bipartite using BFS
def is_bipartite(V, adj):
    # Initialize all as -1 (uncolored)
    color = [-1] * V

    for i in range(V):

        # If the vertex is uncolored, start BFS from it
        if color[i] == -1:

            # Assign first color (0)
            color[i] = 0
            q = deque([i])

            while q:
                u = q.popleft()

                # Traverse all adjacent vertices
                for v in adj[u]:

                    # If the adjacent vertex is uncolored,
                    # assign alternate color
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)

                    # If the adjacent vertex has the same color,
                    # graph is not bipartite
                    elif color[v] == color[u]:
                        return False

                        # If no conflicts in coloring, graph is bipartite
    return True


if __name__ == "__main__":
    # Graph Structure:
    # 0 - 1
    # |   |
    # 3 - 2
    V = 4
    adj = [[] for _ in range(V)]

    # Adding edges (undirected)
    adj[0].append(1)
    adj[1].append(0)
    adj[1].append(2)
    adj[2].append(1)
    adj[2].append(3)
    adj[3].append(2)
    adj[3].append(0)
    adj[0].append(3)

    if is_bipartite(V, adj):
        print("true")
    else:
        print("false")
