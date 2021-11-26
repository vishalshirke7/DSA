"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

"""
"""
class Solution {
    public int longestSubstring(String s, int k) {
        return longestSubstringUtil(s, 0, s.length(), k);
    }

    int longestSubstringUtil(String s, int start, int end, int k) {
        if (end < k) return 0;
        int[] countMap = new int[26];
        // update the countMap with the count of each character
        for (int i = start; i < end; i++)
            countMap[s.charAt(i) - 'a']++;
        for (int mid = start; mid < end; mid++) {
            if (countMap[s.charAt(mid) - 'a'] >= k) continue;
            int midNext = mid + 1;
            while (midNext < end && countMap[s.charAt(midNext) - 'a'] < k) midNext++;
            return Math.max(longestSubstringUtil(s, start, mid, k),
                    longestSubstringUtil(s, midNext, end, k));
        }
        return (end - start);
    }
}
"""

def longestSubstringUtil(input_str, start, end, repeats):
    if end < repeats:
        return 0
    char_map = dict()
    for index in range(start, end):
        char_map[input_str[index]] = char_map.get(input_str[index], 0) + 1    
    for index in range(start, end):
        if char_map[input_str[index]] >= repeats:
            continue
        next_start = index + 1
        return max(longestSubstringUtil(input_str, start, index, repeats), longestSubstringUtil(input_str, next_start, end, repeats))
    return end - start

def longestSubstring(s, k):
    return longestSubstringUtil(s, 0, len(s), k)


print(longestSubstring('aaabb', 3))
print(longestSubstring('ababbc', 2))
print(longestSubstring('bbaaacbd', 3))
