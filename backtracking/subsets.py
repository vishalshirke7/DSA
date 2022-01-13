"""
https://leetcode.com/problems/subsets/
"""

# O(2 ^ n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        size = len(nums)        
        def recurse(index, path):
            if index >= size:
                result.append(path)
                return
            inc_path = path + [nums[index]]
            recurse(index + 1, inc_path)
            recurse(index + 1, path)
        recurse(0, [])
        return result


"""public List<List<Integer>> subsets(int[] nums) {
            List<List<Integer>> list = new ArrayList<>();
            Arrays.sort(nums);
            backtrack(list, new ArrayList<>(), nums, 0);
            return list;
        }
        
        private void backtrack(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
            list.add(new ArrayList<>(tempList));
            for(int i = start; i < nums.length; i++){
                tempList.add(nums[i]);
                backtrack(list, tempList, nums, i + 1);
                tempList.remove(tempList.size() - 1);
            }
        }"""        