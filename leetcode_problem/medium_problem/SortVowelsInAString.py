class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ["A","I","E","O","U","a","i","o","e","u"]
        index_array = []
        sort_array = []
        count1 = 0
        for i in range(0,len(vowels)):
            if vowels[i] in s:
                count1 = count1 + 1
        if count1 == 0:
            return s
        for i in range(0,len(s)):
            if s[i] in vowels:
                sort_array.append(s[i])
                index_array.append(i)
        sorted_array = sorted(sort_array)
        count = 0
        temp = list(s)
        for i in index_array:
            temp[i] = sorted_array[count]
            count = count + 1
        return "".join(temp)