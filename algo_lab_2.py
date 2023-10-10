import unittest


def sum_of_three(arr, P):
    n = len(arr)
    if n < 3:
        return False
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            desired_number = P - arr[i] - arr[j]
            count += 1
            if desired_number in arr and desired_number != arr[i] and desired_number != arr[j]:
                print(count)
                return True
    print(count)
    return False


class TestSumOfThree(unittest.TestCase):
    def test_normal_array(self):
        array = [1, 2, 3]
        self.assertTrue(sum_of_three(array, 6))

    def test_short_array(self):
        array = [1, 4]
        self.assertFalse(sum_of_three(array, 6))

    def test_wrong_P(self):
        array = [1, 2, 3]
        self.assertFalse(sum_of_three(array, 7))

    if __name__ == "__main__":
        unittest.main()
