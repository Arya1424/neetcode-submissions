class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=[[] for i in range(n)]

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit=[False]*n

        def dfs(node):
            for nei in graph[node]:
                if not visit[nei]:
                    visit[nei]=True
                    dfs(nei)

        res=0
        for i in range(n):
            if not visit[i]:
                visit[i]=True
                dfs(i)
                res+=1

        return res