class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = []
        nums = list(map(str, nums))

        def char_order(prefix,char):
            if char.isdi

        def prefix_sort(prefix, num_list):
            if num_list[0] == num_list[-1]:
                for num in num_list:
                    res.append(prefix + num)

