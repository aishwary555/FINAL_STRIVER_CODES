class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getPreorder(self, root):
        # List to store the preorder traversal result
        preorder = []

        # Pointer to the current node, starting with the root
        cur = root

        # Iterate until the current node becomes None
        while cur is not None:
            # If the current node has no left child
            if cur.left is None:
                # Add the value of the current node to the preorder list
                preorder.append(cur.val)

                # Move to the right child
                cur = cur.right
            else:
                # If the current node has a left child
                # Create a pointer to traverse to the rightmost node in the left subtree
                prev = cur.left

                # Traverse to the rightmost node in the left subtree
                # or until we find a node whose right child is not yet processed
                while prev.right and prev.right != cur:
                    prev = prev.right

                # If the right child of the rightmost node is None
                if prev.right is None:
                    # Set the right child of the rightmost node to the current node
                    prev.right = cur

                    # Preorder print happens here (before going to the left)
                    preorder.append(cur.val)  # <-- This line ensures preorder

                    # Move to the left child
                    cur = cur.left
                else:
                    # If the right child of the rightmost node is not None
                    # Reset the right child to None
                    prev.right = None

                    # Move to the right child
                    cur = cur.right

        # Return the resulting preorder traversal list
        return preorder


# Main function
if __name__ == "__main__":
    # Construct the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)

    # Create an instance of the Solution class
    sol = Solution()

    # Perform Morris Preorder Traversal
    preorder = sol.getPreorder(root)

    # Print the result
    print("Binary Tree Morris Preorder Traversal:", end=" ")
    for val in preorder:
        print(val, end=" ")
    print()
                           
                        