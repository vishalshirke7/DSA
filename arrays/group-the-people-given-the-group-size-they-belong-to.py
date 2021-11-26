"""
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""




def groupThePeople(groupSizes):
        output = list()
        size_to_index_map = dict()
        for index in range(len(groupSizes)):
            group_size = groupSizes[index]
            if group_size in size_to_index_map:
                if len(size_to_index_map[group_size]) == group_size:
                    output.append(size_to_index_map[group_size])
                    size_to_index_map[group_size] = [index]
                else:
                    size_to_index_map[group_size].append(index)
            else:
            	size_to_index_map[group_size] = [index]
        output += size_to_index_map.values()
        return output


print('Output', groupThePeople([2,1,3,3,3,2]))