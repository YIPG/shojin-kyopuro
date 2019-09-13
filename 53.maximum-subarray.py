#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0]*n
        dp[0]=nums[0]
        MAX = dp[0]

        for i in range(1,n):
            print(dp[i-1])
            dp[i]=nums[i]
            if dp[i-1]>0:
                dp[i]+=dp[i-1]
            MAX = max(MAX,dp[i])

        return MAX

