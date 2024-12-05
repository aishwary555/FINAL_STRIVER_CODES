# TreeNode structure
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getInorder(self, root):
        # Vector to store the
        # inorder traversal result
        inorder = []
        # Pointer to the current node,
        # starting from the root
        cur = root

        # Loop until the current
        # node is not None
        while cur is not None:
            # If the current node's
            # left child is None
            if cur.left is None:
                # Add the value of the current
                # node to the inorder list
                inorder.append(cur.val)
                # Move to the right child
                cur = cur.right
            else:
                # If the left child is not None,
                # find the predecessor (rightmost node
                # in the left subtree)
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right

                # If the predecessor's right child
                # is None, establish a temporary link
                # and move to the left child
                if prev.right is None:
                    prev.right = cur
                    cur = cur.left
                else:
                    # If the predecessor's right child
                    # is already linked, remove the link,
                    # add the current node to inorder list,
                    # and move to the right child
                    prev.right = None
                    inorder.append(cur.val)
                    cur = cur.right

        # Return the inorder
        # traversal result
        return inorder


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    sol = Solution()

    inorder = sol.getInorder(root)

    print("Binary Tree Morris Inorder Traversal:", end=" ")
    for val in inorder:
        print(val, end=" ")
    print()
                           
                        