"""
https://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/
"""

def findMaxZeroCount(arr, n):
	original_zero_count = 0
	current_diff = max_diff = 0
	for val in arr:
		if val == 0:
			original_zero_count += 1
		current_val = 1 if val == 1 else -1
		current_diff = max(current_val, current_diff + current_val)
		max_diff = max(current_diff, max_diff)
	max_diff = max(0, max_diff)
	return original_zero_count + max_diff

print('Output', findMaxZeroCount([0, 1, 0, 0, 1, 1, 0], 7))

"""
    public static long getMaximumZeros(Integer[] arr, Map<Integer, Long> freqMap) {
        long MAX_NUM_ZEROS = freqMap.get(0);
        int wL = 0, wR = 0;
        int NUM_ZEROS_IN_CURRENT_SUB_ARR = 0;
        int start = 0, end = 0;

        while (wR < arr.length) {
            if (arr[wR] == 0) {
                wR++;
                wL = wR;
            } else {
                NUM_ZEROS_IN_CURRENT_SUB_ARR = 0;
                while (wR < arr.length && arr[wR] != 0) {
                    NUM_ZEROS_IN_CURRENT_SUB_ARR++;
                    wR++;
                }
                if (MAX_NUM_ZEROS < freqMap.get(0) + NUM_ZEROS_IN_CURRENT_SUB_ARR) {
                    MAX_NUM_ZEROS = freqMap.get(0) + NUM_ZEROS_IN_CURRENT_SUB_ARR;
                    start = wL;
                    end = wR - 1;
                }
            }
        }
        return MAX_NUM_ZEROS;
    }
}

"""