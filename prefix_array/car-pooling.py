"""
https://leetcode.com/problems/car-pooling/
"""
#OWN O(nlogn)
def carPooling(trips, capacity):
    trip_members = dict()
    for trip in trips:
        kilometers, start, end = trip[0], trip[1], trip[2]
        trip_members[start] =  trip_members.get(start, 0) + kilometers
        trip_members[end] = trip_members.get(end, 0) - kilometers
    trip_members = sorted(trip_members.items(), key=lambda x:x[0])
    prefix_sum = [0] * len(trip_members)
    prefix_sum[0] = trip_members[0][1]
    for index in range(1, len(trip_members)):
        prefix_sum[index] = trip_members[index][1] + prefix_sum[index - 1]
    for val in prefix_sum:
        if val > capacity:
            return False
    return True


    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        pas = 0
        for loc in lst:
            pas += loc[1]
            if pas > capacity:
                return False
        return True
                
"""
O(n)
public boolean carPooling(int[][] trips, int capacity) {    
  int stops[] = new int[1001]; 
  for (int t[] : trips) {
      stops[t[1]] += t[0];
      stops[t[2]] -= t[0];
  }
  for (int i = 0; capacity >= 0 && i < 1001; ++i) capacity -= stops[i];
  return capacity >= 0;
}
"""    

print('Output', carPooling([[2,1,5],[3,3,7]], 4))