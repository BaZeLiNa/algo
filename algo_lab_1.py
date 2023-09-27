import unittest


def is_subarray(nums1, nums2):
    try:
        index = -1
        for num in nums1:
            index = nums2.index(num, index + 1)
        return True
    except ValueError:
        return False


class TestIsSubarray(unittest.TestCase):
    def test_subarray_found(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4]
        self.assertTrue(is_subarray(nums1, nums2))

    def test_subarray_not_found(self):
        nums1 = [4, 2]
        nums2 = [1, 2, 3, 4]
        self.assertFalse(is_subarray(nums1, nums2))

    def test_subarray_found_in_other_places(self):
        nums1 = [1, 3, 5]
        nums2 = [1, 2, 3, 4, 5]
        self.assertTrue(is_subarray(nums1, nums2))


if __name__ == "__main__":
    unittest.main()
