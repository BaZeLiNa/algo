import unittest

from src.algo_lab_7 import count_paths


class TestCountPaths(unittest.TestCase):

    def test_test1_corridor(self):
        corridor = [
            ['a', 'b'],
            ['c', 'd'],
            ['e', 'f'],
            ['g', 'h']
        ]
        W, H = 2, 4
        result = count_paths(W, H, corridor)
        self.assertEqual(2, result)

    def test_test2_corridor(self):
        corridor = [
            ['a', 'b', 'b'],
            ['c', 'd', 'c'],
            ['c', 'b', 'a']
        ]
        W, H = 3, 3
        result = count_paths(W, H, corridor)
        self.assertEqual(4, result)

    def test_test3_corridor(self):
        corridor = [
            ['a', 'b', 'a', 'c', 'a', 'a'],
            ['b', 'c', 'a', 'd', 'e', 'f'],
            ['d', 'a', 'c', 'f', 'g', 'h'],
            ['c', 'd', 'a', 'b', 'f', 'c']
        ]
        W, H = 6, 4
        result = count_paths(W, H, corridor)
        self.assertEqual(83, result)


if __name__ == "__main__":
    unittest.main()
