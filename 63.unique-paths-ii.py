#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
class Solution:
#     def uniquePath(self,m,n):
#         # m is num of row, n is num of col
#         dp=[1]*n
#         for _ in range(1,m):
#             for i in range(1,n):
#                 dp[i]+=dp[i-1]
#         print(dp)
#         return dp[-1]
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         row = len(obstacleGrid)
#         col = len(obstacleGrid[0])
#         obstacle = []
#         for i,r in enumerate(obstacleGrid):
#             for j,e in enumerate(r):
#                 if e == 1:
#                     obstacle.append((i,j))
#         # v_all(start-goal paths) + v_obs(obstacle-obstacle paths) - v_mid_obs(start-each obstacle-goal obstacke)
#         v_all = self.uniquePath(row,col) if obstacleGrid[-1][-1] == 0 and obstacleGrid[0][0]==0 else 0
#         print("row is {}, col is {}".format(row,col))
#         v_obs = 0
#         if len(obstacle)>=2:
#             dist_l = []
#             for i in range(len(obstacle)):
#                 for j in range(1,len(obstacle)):
#                     dist_l.append((1+abs(obstacle[i][0]-obstacle[j][0]), 1+abs(obstacle[i][1] - obstacle[j][1])))
#             for d in dist_l:
#                 v_obs += self.uniquePath(d[0], d[1])
#         v_mid_obs = 0
        
#         if len(obstacle)!=0:
#             for obs in obstacle:
#                 r_dist = row-obs[0]
#                 l_dist = col-obs[1]
#                 tmp_v = self.uniquePath(obs[0]+1,obs[1]+1)*self.uniquePath(r_dist,l_dist)
#                 v_mid_obs+=tmp_v
#         print(v_all,v_obs,v_mid_obs)
#         ans = v_all + v_obs - v_mid_obs
#         return max(0,ans)

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h,w = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1]*w
        dp_h = [1]*h
        
        for j in range(h):
            if obstacleGrid[j][0]==1:
                dp_h = [1]*j+[0]*(h-j)
                break
        for i in range(1,h):
            for j in range(w):
                if obstacleGrid[i][j]==0:
                    if j==0:
                        dp[j]=dp_h[i]
                    else:
                        dp[j]+=dp[j-1]
                    print(dp)
                else:
                    dp[j]=0
        return dp[-1]
        
