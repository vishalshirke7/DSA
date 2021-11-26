"""
https://leetcode.com/problems/jump-game-iii/

"""

def Dfs(array, index, visited):
	if index >= len(array) or index < 0 or index in visited:
		return False
	if array[index] == 0:
		return True
	visited.add(index)
	return Dfs(array, index - array[index], visited) or Dfs(array, index + array[index], visited)

def canReach(arr, start):
	return Dfs(arr, start, set())


# print(canReach([4,2,3,0,3,1,2], 5))
print(canReach([4,2,3,0,3,1,2], 0))
# print(canReach([3,0,2,1,2], 2))


"""
BFS

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        bfs = deque([start])
        visited = [False] * n
        while bfs:
            i = bfs.popleft()
            if arr[i] == 0: return True  # Found result
            if visited[i]: continue
            visited[i] = True
            if i - arr[i] >= 0: bfs.append(i - arr[i])
            if i + arr[i] < n: bfs.append(i + arr[i])
        return False

"""