import collections
from typing import List
class Node:
    def __init__(self, value, level):
        self.value = value
        self.children = []
        self.level = level
    def add_child(self, child_node):
        self.children.append(child_node)


def build_combination_tree(nums: List[int]) -> Node:

    root = Node(value=[], level=0)

    def _recursion_build(current_node, start_index):

        for i in range(start_index, len(nums)):
            new_combination = list(current_node.value)
            new_combination.append(nums[i])

            child_node = Node(value=new_combination, level= current_node.level + 1)
            current_node.children.append(child_node)

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

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:

        root_of_subsets_tree = build_combination_tree(nums)

        all_non_empty_subsets = get_combination_from_tree(root_of_subsets_tree)

        print(all_non_empty_subsets)    