"""
https://www.interviewbit.com/old/problems/zigzag-string/
"""
#OWN
def convert(A, B):
    size = len(A)
    rows = B - 1
    char_list = list()
    if B <= 1:
        return A
    for index in range(B):
        cur = index
        cnt = 0
        while cur < size:
            if cnt % 2 == 0:
                rem = index if rows - index == 0 else rows - index
            else:
                rem = rows if index == 0 else index
            jump = (rem - 1) * 2 + 2
            char_list.append(A[cur])
            cur += jump
            cnt += 1
    return "".join(char_list)

"""class Solution {
    public String convert(String s, int numRows) {

        if (numRows == 1) return s;

        StringBuilder ret = new StringBuilder();
        int n = s.length();
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < n; j += cycleLen) {
                ret.append(s.charAt(j + i));
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n)
                    ret.append(s.charAt(j + cycleLen - i));
            }
        }
        return ret.toString();
    }
}"""

print('Output', convert('ABCD', 2))
print('Output', convert('ABCDEFGHIJKLMNOPQRS', 6))
print('Output', convert('PAYPALISHIRING', 3))