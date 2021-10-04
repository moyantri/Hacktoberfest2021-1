def longestPalindrome(self, s: str) -> str:
        res = s[0]
        max_length=1
        for i in range(len(s)):
			# if max_length>len(s)-i: break
            for j in range(len(s)-1,i+max_length-1,-1):
                if s[i:j+1]==s[i:j+1][::-1]:
                    max_length=j-i
                    res=s[i:j+1]
                    break
        return res
        
#Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.        
