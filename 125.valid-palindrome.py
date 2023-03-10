# @before-stub-for-debug-begin
from python3problem125 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]

# @lc code=end

