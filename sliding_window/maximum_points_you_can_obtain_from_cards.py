"""
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
https://www.interviewbit.com/old/problems/pick-from-both-sides/
"""

def maxScore(cardPoints, k):
    size = len(cardPoints) - k
    S = sum(cardPoints[size:])
    ans = S
    for i in range(0, k):
        S += cardPoints[i]
        S -= cardPoints[i+size]
        ans = max(ans, S)
    return ans

print(maxScore([1,2,3,4,5,6,1], 3))	
print(maxScore([2,2,2], 2))
print(maxScore([9,7,7,9,7,7,9], 7))	
print(maxScore([1,1000,1], 1))
print(maxScore([1,79,80,1,1,1,200,1], 3))
print(maxScore([96,90,41,82,39,74,64,50,30], 8))


"""
PREFIX SUM
public int maxScore(int[] cp, int k) {
    int n = cp.length;
    int leftsum = 0;
    for (int i = 0; i < k; i++) {
        leftsum += cp[i];
    }
    int max = leftsum;
    int rightsum = 0;

    for (int i = 0; i < k; i++) {
        leftsum  -= cp[k - 1 - i];
        rightsum += cp[n - 1 - i];
        max = Math.max(max, leftsum + rightsum);
    }

    return max;
}
"""
"""
def maxScore(cardPoints, k):
    size = len(cardPoints) - k
    S = sum(cardPoints[size:])
    ans = S
    for i in range(0, k):
        S += cardPoints[i]
        S -= cardPoints[i+size]
        ans = max(ans, S)
    return ans
"""
"""
    def maxScore(self, A: List[int], K: int) -> int:
        N = len(A)
        i = 0
        j = N - K
        total = sum(A[j:])
        best = total
        for _ in range(K):  # slide window by K 
            total += A[i] - A[j]
            best = max(best, total)
            i += 1
            j += 1
        return best
"""
"""
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubArraySum = float('inf')
        j = curr = 0
        
        for i, v in enumerate(cardPoints):
            curr += v
            if i - j + 1 > size:
                curr -= cardPoints[j]
                j += 1
            if i - j + 1 == size:    
                minSubArraySum = min(minSubArraySum, curr)
				
        return sum(cardPoints) - minSubArraySum
"""
"""
def maxScore(self, cardPoints, k: int) -> int:
        size = len(cardPoints) - k
        i, j = 0, size
        curr_sum = min_sub_sum = sum(cardPoints[i:j])
        for i in range(k):
            curr_sum = curr_sum + cardPoints[j] - cardPoints[i]
            min_sub_sum = min(min_sub_sum, curr_sum)
            j += 1
        return sum(cardPoints) - min_sub_sum

"""        