from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
            
        m, n = len(grid), len(grid[0])
        count = 0
        
        # 상하좌우 방향 정의
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # BFS 헬퍼 함수: (r, c)에서 시작해서 연결된 모든 땅을 '0'으로 가라앉힘
        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = '0'  # 큐에 넣자마자 방문 처리(가라앉힘)
            
            while q:
                curr_r, curr_c = q.popleft()
                
                # 4방향 탐색
                for dr, dc in directions:
                    nr, nc = curr_r + dr, curr_c + dc
                    
                    # 1. 맵 범위 안에 있고
                    # 2. 그곳이 땅('1') 이라면?
                    # => 큐에 (nr, nc)를 넣고, 땅을 '0'으로 바꿔라!

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        q.append([nr, nc])
                        grid[nr][nc] = '0'



        # 지도 전체를 스캔
        for i in range(m):
            for j in range(n):
                # 땅('1')을 발견하면
                if grid[i][j] == '1':
                    count += 1   # 섬 개수 증가
                    bfs(i, j)    # 연결된 땅을 모두 가라앉힘
                    
        return count









if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: 예시 1 (섬 1개)
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print("TC 1:", sol.numIslands(grid1)) # Expected: 1
    
    # Test Case 2: 예시 2 (섬 3개)
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("TC 2:", sol.numIslands(grid2)) # Expected: 3
    
    # Test Case 3: 모두 물인 경우
    grid3 = [
        ["0","0"],
        ["0","0"]
    ]
    print("TC 3:", sol.numIslands(grid3)) # Expected: 0