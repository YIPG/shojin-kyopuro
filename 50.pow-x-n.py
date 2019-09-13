#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            n*=-1
            x=1/x
        if n&1==0:
            return self.myPow(x*x, n>>1)
        return x*self.myPow(x, n-1)
        

