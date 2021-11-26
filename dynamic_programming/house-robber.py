"""
https://leetcode.com/problems/house-robber/
"""

"""https://leetcode.com/problems/house-robber/discuss/846004/Python-4-lines-easy-dp-solution-explained"""

def rob(nums):
    odd_sum = even_sum = 0
    for index in range(len(nums)):
        if index % 2 == 0:
            even_sum = max(even_sum + nums[index], odd_sum)
        else:
            odd_sum = max(odd_sum + nums[index], even_sum)
    return max(odd_sum, even_sum)



print('Output', rob([1,2,3,1]))
print('Output', rob([2,7,9,3,1]))


"""
dp[i] = Math.max(dp[i-1], dp[i-2]+num[i-1])

view sourceprint?
public class CrazyForCode {
    public int steal(int[] num) {
        if(num==null || num.length==0){
            return 0;
        }
        int[] dp= new int[num.length+1];
        dp[0]=0;
        dp[1]=num[0];
        for(int i=2; i<=num.length;i++){
            dp[i] =Math.max(dp[i-1],num[i-1]+dp[i-2]);
        }
        return dp[num.length];
    }
}

"""