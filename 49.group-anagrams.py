# @before-stub-for-debug-begin
from python3problem49 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

from collections import defaultdict

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(s))
            ans[sorted_word].append(s)
        return ans.values()

# @lc code=end

