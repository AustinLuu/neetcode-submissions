import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        for i in range(0,len(clean_str)//2):
            if clean_str[i] != clean_str[-1-i]:
                return False
        return True