# Given two strings, str1 and str2, find the shortest substring in str1 such that str2 is a subsequence of that substring.
# A substring is defined as a contiguous sequence of characters within a string. A subsequence is a sequence that can be 
# derived from another sequence by deleting zero or more elements without changing the order of the remaining elements.
# str1 = “abbcb”
# str2 = “ac”
# In this example, “abbc” is a substring of str1, from which we can derive str2 simply by deleting both the instances of the character 
# b. Therefore, str2 is a subsequence of this substring. Since this substring is the shortest among all the substrings in which 
# str2 is present as a subsequence, the function should return this substring, that is, “abbc”.

class Solution:
    def min_window(str1, str2):
    
        # Replace this placeholder return statement with your code
        n1 = len(str1)
        n2 = len(str2)
        min_len = float('inf')
        min_subseq = ''
        i1 = 0
        i2 = 0
        
        while i1<n1:
            if str1[i1] == str2[i2]:
                i2+=1
                if i2==n2:
                    i2-=1
                    l=i1
                    r=i1
                    while i2>=0:
                        if str1[l]==str2[i2]:
                            i2-=1
                        l-=1
                    l+=1
                    if r-l < min_len:
                        min_len = r-l
                        min_subseq = str1[l:r+1]
                    i1 = l
                    i2 = 0
            i1+=1
        return min_subseq