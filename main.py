from leetcode_problem import twoSum, powerOfTwo, checkPerfectNumber, palindromeNumber,romanToInteger, sqrtX,happyNumber
from leetcode_problem import lengthOfLastNumber,singleNumber,uglyNumber,powerOfThree,powerOfFour,addDigit,bestTimeToSell,FizzBuzz
from leetcode_problem import MaximumProductofThreeNumbers , addStrings,findallnumberInArray,ValidParentheses,SymmetricTree
from collections import deque
from leetcode_problem import ValidPerfectSquare,maxproductoftwonumberinarray,FindtheIndexoftheFirstOccurrenceinaString,plusOne
from leetcode_problem import SearchInsertPosition,containdup,validArangam,IsSubsequence, MultiplyStrings,removeElemental
from leetcode_problem.medium_problem import longetSubstring,DivideTwoIntegers
from leetcode_problem import missingNumber
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def list_to_tree(arr):
#     if not arr:
#         return None
#     root = TreeNode(arr[0])
#     queue = deque([root])
#     i = 1
#     while queue and i < len(arr):
#         node = queue.popleft()
#         if arr[i] is not None:
#             node.left = TreeNode(arr[i])
#             queue.append(node.left)
#         i += 1
#         if i < len(arr) and arr[i] is not None:
#             node.right = TreeNode(arr[i])
#             queue.append(node.right)
#         i += 1
#     return root
# 1.two sum problem

# nums = [3,2,4]
# target = 7
# s = twoSum.Solution()
# print(s.twoSum(nums,target))

# 2. power of two problem

# n = 3
# s = powerOfTwo.Solution()
# print(s.isPowerOfTwo(n))

# 3. check perfect number
# s = checkPerfectNumber.Solution()
# print(s.checkPerfectNumber2(99999995))

# 4.check palindrome number
# x = 121
# s = palindromeNumber.Solution()
# print(s.isPalindrome(x))

# 5.convert roman to integer 
# target: str = "ILXMV"
# s = romanToInteger.Solution()
# print(s.romanToInt(target))

# 6. find sqrt(x)
# x = 8
# s = sqrtX.Solution()
# print(s.mySqrt(x))

# 7. check happy number

# n = 19
# s = happyNumber.Solution()
# print(s.isHappy(n))

# 8. check length of last number
# thinh = "aaabbb"
# s = lengthOfLastNumber.Solution()
# print(s.lengthOfLastWord(thinh))

# 9 . single number
# nums = [1,1,1,1,2,3,1,2,3,4]
# s = singleNumber.Solution()
# # print(s.singleNumber(nums))
# print(s.singleNumber2(nums))

# 10 . Ugly Number
# num = 30
# s = uglyNumber.Solution()
# print(s.isUgly(num))

# 11.power of three
# num = 27
# s = powerOfThree.Solution()
# print(s.isPowerOfThree(num))

# 12.power of four
# num = 16
# s = powerOfFour.Solution()
# print(s.isPowerOfFour(num))

# 13.add digit
# num = 38
# s = addDigit.Solution()
# print(s.addDigits(num))

# 14.best time to sell
# stock = [7,1,3,5,6,2]
# s = bestTimeToSell.Solution()
# print(s.maxProfit(stock))

# 15.Fizz Buzz
# n = 15
# s = FizzBuzz.Solution()
# print(s.fizzBuzz(n))

# 16.Maxium ...
# n=[1,5,4,2,3,6,8,112,-12]
# s = MaximumProductofThreeNumbers.Solution()
# print(s.maximumProduct(n))

# 17.add strings
# n = "123141123124121244578909876543223412424"
# a = "12361294178352382"
# s= addStrings.Solution()
# print(s.addStrings(a,n))

# 18.find number
# input = [1,4,2,5,6,3,214,5,12,3,14,1]
# s = findallnumberInArray.Solution()
# print(s.findDisappearedNumbers(input)) 

# 19.valid ...
# input = "([{}))"
# s = ValidParentheses.Solution()
# print(s.isValid(input))

# 20.symmectric
# root = list_to_tree([1,2,2,3,4,3,4])
# s = SymmetricTree.Solution()
# print(s.isSymmetric(root))

# 21.valid pefect
# num = 16
# s = ValidPerfectSquare.Solution()
# print(s.isPerfectSquare(num))

# 22. max product 2
# num = [1,124,15,1,24,12,41,51,3,41,3,135,3]
# s = maxproductoftwonumberinarray.Solution()
# print(s.maxProduct(num))

# 23. find...
# haystack = "hellollolploplopl"
# needle = "lopp"
# s = FindtheIndexoftheFirstOccurrenceinaString.Solution()
# print(s.strStr(haystack,needle))

# 24.search index
# nums=[1,3,4,5,6,100]
# target = 13
# s = SearchInsertPosition.Solution()
# print(s.searchInsert(nums,target))

# 25.contain dup
# nums = [1,2,31,3,4,13,3121,5]
# s = containdup.Solution()
# print(s.containsDuplicate(nums))

# 26.valid anagram
# yas = "a12314dfaw"
# t = "nad1234faws"
# s = validArangam.Solution()
# print(s.isAnagram(yas,t))

# 27.is sub..
# l = "aaaaba"
# t = "bbbbaaaaba"
# s = IsSubsequence.Solution()
# print(s.isSubsequence2(l,t))

# 28.longest.medium
# gice = "abcabcbb"
# s = longetsubstring.Solution()
# print(s.lengthOfLongestSubstring(gice))

# 29.muilti
# a = "124"
# b = "14214"
# s = MultiplyStrings.Solution()
# print(s.multiply(a,b))

# 30.divine 2 int
# a = 1241245621
# b = 247
# s = DivideTwoIntegers.Solution()
# print(s.divide(a,b))

# 32.remove elemental
# nums = [1,14,1,5,1,234,1,412,3,12,1,292025,45,142]
# val = 1
# s = removeElemental.Solution()
# print(s.removeElement(nums,val))

# 33.plus one
# numinlist = [1,2,3,5,4,5,6]
# s = plusOne.Solution()
# print(s.plusOne2(numinlist))

#34.missing number
nums = [0,1,2,3,4,5,7,8,9]
s = missingNumber.Solution()
print(s.missingNumber(nums))