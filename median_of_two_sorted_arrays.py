"""
Median of Two Sorted Array
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""


def find_median_sorted_array(nums1, nums2):
    """
    :param nums1:
    :param nums2:
    :return:
    """
    if len(nums1) % 2:
        nums1_median = nums1[int(len(nums1)/2)]
    else:
        nums1_median = sum(nums1[(int(len(nums1)/2)-1):(int(len(nums1)/2)+1)])/2
    if len(nums2) % 2:
        nums2_median = nums2[int(len(nums2)/2)]
    else:
        nums2_median = sum(nums2[(int(len(nums2)/2)-1):(int(len(nums2)/2)+1)])/2
    if nums1_median < nums2_median:
        min_median = nums1_median
        max_median = nums2_median
    else:
        min_median = nums2_median
        max_median = nums1_median
    if min_median == max_median:
        num_median = min_median
    else:
        num = []
        for i in range(len(nums1)-1, -1, -1):
            if min_median <= nums1[i] <= max_median:
                num.append(nums1[i])
        for i in range(len(nums2)-1, -1, -1):
            if min_median <= nums2[i] <= max_median:
                num.append(nums2[i])
        num_median = sum(num) / len(num)
    return num_median


if __name__ == '__main__':
    num_array1 = []
    num_array2 = [2, 3]
    median = find_median_sorted_array(nums1=num_array1, nums2=num_array2)
    print(median)
