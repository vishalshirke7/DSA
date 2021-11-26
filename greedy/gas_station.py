"""
https://www.interviewbit.com/problems/gas-station/
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        sumo=0
        fuel=0
        start=0
        for i in range(len(gas)):
            sumo = sumo + (gas[i] - cost[i])
            fuel = fuel + (gas[i] - cost[i])
            if fuel<0:
                fuel=0
                start=i+1
        if sumo>=0:
            return (start%len(gas))
        else:
            return -1



class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        if sum(B)>sum(A): return -1
        n=len(A)
        
        ans=total=cost=0
        for i in range(n):
            total+=A[i]
            cost+=B[i]
            if cost>total:
                ans=(i+1)
                total=cost=0
        return ans            