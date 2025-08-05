import collections
from typing import List

MOD = 10**9 + 7
SUM = 0  # Global to track total power

class Node:
    def __init__(self, value, level):
        self.value = value
        self.children = []
        self.level = level
    def add_child(self, child_node):
        self.children.append(child_node)

def build_combination_tree_and_sum(nums: List[int]) -> Node:
    global SUM
    root = Node(value=[], level=0)

    def _recursion_build(current_node, start_index):
        global SUM
        for i in range(start_index, len(nums)):
            new_combination = list(current_node.value)
            new_combination.append(nums[i])

            # ✅ Tính power ở đây
            mx = max(new_combination)
            mn = min(new_combination)
            power = (mx * mx * mn) % MOD
            SUM = (SUM + power) % MOD

            child_node = Node(value=new_combination, level=current_node.level + 1)
            current_node.add_child(child_node)

            _recursion_build(child_node, i + 1)

    _recursion_build(root, 0)
    return root

def get_combination_from_tree(root_node):
    all_combination = []

    def dfs_traverse(node):
        if node.value:
            all_combination.append(node.value)

        for child in node.children:
            dfs_traverse(child)

    dfs_traverse(root_node)
    return all_combination

def power(subset: List[int]) -> int:
    return max(subset)**2 * min(subset)
# class Solution:
#     def sumOfPower(self, nums: List[int]) -> int:

#         root_of_subsets_tree = build_combination_tree_and_sum(nums)

#         # all_non_empty_subsets = get_combination_from_tree(root_of_subsets_tree)

#         return SUM    

# Chuẩn leetcode
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        self.total = 0  # Dùng self thay vì global

        def build_tree_and_sum(current_node, start_index):
            for i in range(start_index, len(nums)):
                new_comb = list(current_node.value)
                new_comb.append(nums[i])

                # Tính power của tập con
                mx = max(new_comb)
                mn = min(new_comb)
                power = (mx * mx * mn) % MOD
                self.total = (self.total + power) % MOD

                # Tạo node con và tiếp tục
                child_node = Node(value=new_comb, level=current_node.level + 1)
                current_node.add_child(child_node)
                build_tree_and_sum(child_node, i + 1)

        root = Node(value=[], level=0)
        build_tree_and_sum(root, 0)
        return self.total
