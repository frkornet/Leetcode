# Leetcode:
#
# 4. Median of Two Sorted Arrays (Hard)
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity 
# should be O(log(m+n)).
#
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#

from typing import List

class Solution:
    def index_le(self, l1, threshold):
        n = len(l1)
        start = 0
        end = n - 1

        assert l1[start] <= threshold, "l1[start] needs to be <= threshold!"
        assert n>0, "empty list not supported!"

        if l1[end] <= threshold:
            return end
        
        while (start < end - 1):
            mid = start + (end - start) // 2
            mid_value = l1[mid]

            if mid_value <= threshold:
                start = mid
            else:
                end = mid
        
        return start

    def process_indices_if_found(self):
        my_sum = 0
        while len(self.indices) > 0 and \
            self.indices[0] < self.merged_index + self.part_len:
            index = self.indices[0] - self.merged_index
            value = self.part[index]
            my_sum += value
            del self.indices[0]
        return my_sum

    def sum_indices(self, l1, l2, indices):
        self.indices = indices

        self.sommetje = 0
        l1_index = l2_index = 0
        self.merged_index = 0
        l1len = len(l1)
        l2len = len(l2)
        while (l1_index < l1len and l2_index < l2len):
            if l1[l1_index] <= l2[l2_index]:
                l1_start = l1_index
                l1_index = l1_index + self.index_le(l1[l1_start:], l2[l2_index])
                l1_index += 1
                self.part = l1[l1_start:l1_index]
                self.part_len = len(self.part)
                print("l1:", self.part, self.part_len, self.merged_index )
            else:
                l2_start = l2_index
                l2_index = l2_index + self.index_le(l2[l2_start:], l1[l1_index])
                l2_index += 1
                self.part = l2[l2_start:l2_index]
                self.part_len = len(self.part)
                print("l2:", self.part, self.part_len, self.merged_index )

            self.sommetje += self.process_indices_if_found()
            if len(self.indices) == 0:
                return self.sommetje

            self.merged_index += self.part_len

        if l1_index < l1len:
            self.part = l1[l1_index:]
            self.part_len = len(self.part)
            print("l1:", self.part, self.part_len)

        if l2_index < l2len:
            self.part = l2[l2_index:]
            self.part_len = len(self.part)
            print("l2:", self.part, self.part_len )

        self.sommetje += self.process_indices_if_found()
        if len(self.indices) == 0:
            return self.sommetje

        assert 1==2, "Did not find all indices!"

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tot_len = len(nums1) + len(nums2)
        if tot_len % 2 == 0:
            idx1 = (tot_len - 1) // 2
            idx2 = idx1 + 1
            return self.sum_indices(nums1, nums2, [idx1, idx2]) / 2.0
        else:
            idx = (tot_len - 1) // 2
            return float(self.sum_indices(nums1, nums2, [ idx ]))

l1=[0, 0, 1, 10, 11, 12, 13, 14, 15, 16]
l2=[2, 3, 8, 8, 12, 13, 17, 17, 18, 19]
soln = Solution()
median = soln.findMedianSortedArrays(l1, l2)
print(f"median={median}")