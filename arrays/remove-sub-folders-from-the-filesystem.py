"""
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
"""

"https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/discuss/409075/Standard-Python-Trie-solution-(similar-problems-listed)"

def removeSubfolders(folder):
    folder.sort()
    cleaned = [folder[0]]  # first folder is shortest or unique
    prev, prev_n = folder[0]+"/", len(folder[0])+1
    for each in folder[1:]:
        if each[:prev_n] != prev:
            cleaned.append(each)
            prev, prev_n = each + "/", len(each)+1
    return cleaned


print('Output', removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))	