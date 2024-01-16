from typing import List 
from remove_duplicates_from_sorted_array import Solution


def test_removeDuplicates():
    assert Solution().removeDuplicates([1,1,2]) == 2
    assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5