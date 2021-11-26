"""
https://leetcode.com/problems/delete-nodes-and-return-forest/
"""

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        result = list()
        to_delete = set(to_delete)
        
        def dfs(root, parent_del):
            if not root:
                return None
            to_be_del = root.val in to_delete
            if not to_be_del and parent_del:
                result.append(root)
            root.left = dfs(root.left, to_be_del)
            root.right = dfs(root.right, to_be_del)            
            return None if to_be_del else root

        dfs(root, True)
        return result


class Solution(object):
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        res = []
        def walk(root, parent_exist):
            if root is None:
                return None
            if root.val in to_delete:
                root.left = walk(root.left, parent_exist=False)
                root.right = walk(root.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    res.append(root)
                root.left = walk(root.left, parent_exist=True)
                root.right = walk(root.right, parent_exist=True)
                return root
        walk(root, parent_exist=False)
        return res


"""
public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        List<TreeNode> forest = new ArrayList<>();
        if (root == null) return forest;
        Set<Integer> set = new HashSet<>();
        for(int i : to_delete) {
            set.add(i);
        }
        deleteNodes(root, set, forest);
        if (!set.contains(root.val)) {
            forest.add(root);
        }
        return forest;
    }

    private TreeNode deleteNodes(TreeNode node, Set<Integer> set, List<TreeNode> forest) {
        if (node == null) return null;

        node.left = deleteNodes(node.left, set, forest);
        node.right = deleteNodes(node.right, set, forest);

        if (set.contains(node.val)) {
            if (node.left != null) forest.add(node.left);
            if (node.right != null) forest.add(node.right);
            return null;
        }

        return node;
    }
"""            