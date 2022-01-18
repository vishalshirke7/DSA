"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
"""

# def lengthOfLongestSubstring(s):
#     n = len(s)
#     ans = 0
#     # mp stores the current index of a character
#     mp = {}

#     i = 0
#     # try to extend the range [i, j]
#     for j in range(n):
#         if s[j] in mp:
#             i = max(mp[s[j]], i)

#         ans = max(ans, j - i + 1)
#         mp[s[j]] = j + 1

#     return ans

"""
public int lengthOfLongestSubstring(String s) {
        if (s.length()==0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max=0;
        for (int i=0, j=0; i<s.length(); ++i){
            if (map.containsKey(s.charAt(i))){
                j = Math.max(j,map.get(s.charAt(i))+1);
            }
            map.put(s.charAt(i),i);
            max = Math.max(max,i-j+1);
        }
        return max;
    }

"""    

def lengthOfLongestSubstring(s):
    left, right, output, char_map = 0, 0, 0, dict()
    while right < len(s):
        char_map[s[right]] = char_map.get(s[right], 0) + 1
        while char_map[s[right]] > 1:
            char_map[s[left]] -= 1
            left += 1
        output = max(output, right - left + 1)
        right += 1
    return output



print(lengthOfLongestSubstring('abavanalvcaca'))