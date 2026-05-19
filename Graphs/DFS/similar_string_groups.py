class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        visited = [False] * n
        groups = 0

        for i in range(n):
            if not visited[i]:
                self.dfs(strs, visited, i)
                groups += 1

        return groups

    def dfs(self, strs: list[str], visited: list[bool], index: int) -> None:
        visited[index] = True

        for j in range(len(strs)):
            if not visited[j] and self.areSimilar(strs[index], strs[j]):
                self.dfs(strs, visited, j)

    def areSimilar(self, a: str, b: str) -> bool:
        diff = []

        for i in range(len(a)):
            if a[i] != b[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False

        if len(diff) == 0:
            return True

        if len(diff) == 2:
            i, j = diff[0], diff[1]
            return a[i] == b[j] and a[j] == b[i]

        return False