# @before-stub-for-debug-begin
from python3problem217 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# @lc code=end

