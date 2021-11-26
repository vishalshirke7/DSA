"""
https://www.interviewbit.com/problems/balance-array/
"""


def solve(A):
    odd = True
    odd_sum = 0
    even_sum = 0
    for a in A:
        if odd:
            odd_sum += a
        else:
            even_sum += a
        odd = not odd
    ans = 0
    odd = True
    odd_res = 0
    even_res = 0
    for a in A:
        if odd:
            odd_sum -= a
            if even_sum + odd_res == odd_sum + even_res:
                ans += 1
            odd_res += a
        else:
            even_sum -= a
            if even_sum + odd_res == odd_sum + even_res:
                ans += 1
            even_res += a
        odd = not odd
    return ans

def solve(A):
    n = len(A)
    odd = 0
    even = 0
    leftOdd = [0] * n
    rightOdd = [0] * n
    leftEven = [0] * n
    rightEven = [0] * n
    for i in range(n):
        leftOdd[i] = odd
        leftEven[i] = even
        if(i%2 == 0):
            even += A[i]
        else:
            odd += A[i]
    
    odd = 0
    even = 0
    for i in range(n-1, -1, -1):
        rightOdd[i] = odd
        rightEven[i] = even
        if(i%2 == 0):
            even += A[i]
        else:
            odd += A[i]
    
    ans = 0
    for i in range(n):
        if(leftOdd[i] + rightEven[i] == leftEven[i] + rightOdd[i]):
            ans += 1
        
    return ans


print(solve([2, 8, 2, 2, 6, 3]))


public static int solve(ArrayList<Integer> A) {

    int even = 0;
    int odd = 0;
    int count = 0;

    for (int i = 0;i<A.size();i++) {
        if (i%2 == 0) {
            even += A.get(i);
        } else {
            odd += A.get(i);
        }
    }
   

    for (int i = A.size()-1;i>=0;i--) {
        if (i%2==0) {
            even = even - A.get(i);
            if (even == odd) {
                count++;
            }
            odd = odd + A.get(i);
        } else {
            odd = odd - A.get(i);
            if (even == odd) {
                count++;
            }
            even = even + A.get(i);
        }

    }
return count;
}