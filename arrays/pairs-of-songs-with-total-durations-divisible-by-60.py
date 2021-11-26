"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""


def numPairsDivisibleBy60(time):
	complement_map, ans = dict(), 0
	for val in time:
		diff = (60 - (val % 60)) % 60
		ans += complement_map.get(diff, 0)
		print(diff, val % 60, ans)		
		complement_map[val % 60] = complement_map.get(val % 60, 0) + 1
	return ans

"""
for (int t : time) {
    int reducedTime = t % 60;
    int other = (reducedTime == 0) ? 0 : 60 - reducedTime;
    ans += count.getOrDefault(other, 0);
    count.put(reducedTime, count.getOrDefault(reducedTime, 0) + 1);
}
"""

print(numPairsDivisibleBy60([30,20,150,100,40]))
