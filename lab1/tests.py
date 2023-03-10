import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_main(self):
        self.assertEqual(get_last_word_lexicographically("Ana are mere rosii si galbene"), "si")
        self.assertEqual(get_last_word_lexicographically("ab aa ah as ar at azz aza"), "azz")

        self.assertEqual(compute_euclidian_distance(1,5,4,1), 5.0)
        self.assertEqual(compute_euclidian_distance(4, 1, 1, 5), 5.0)

        self.assertEqual(scalar_multiplication([1, 0, 2, 0,3], [1, 2, 0, 3, 1]), 4)
        self.assertEqual(scalar_multiplication([1, 2, 0,3], [1, 2, 3, 1]), 8)

        self.assertEqual(get_unique_words("ana are ana are mere rosii ana"), ["mere", "rosii"])
        self.assertEqual(get_unique_words("un soim pe un pisc cu un soim pe un pisc pix in plisc"), ["cu","pix", "in", "plisc"])

        self.assertEqual(get_twin_number([1,3,4,2,3]), 3)
        self.assertEqual(get_twin_number([1,2,3,4,2]), 2)

        self.assertEqual(get_number_in_majority([2, 8, 7, 1, 4, 5, 0, 3, 1, 2, 2]), "Nu exista nr majoritar")
        self.assertEqual(get_number_in_majority([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]), 2)

        self.assertEqual(get_kth_biggest_number([7, 4, 6, 3, 9, 1], 5), 3)
        self.assertEqual(get_kth_biggest_number([7, 4, 6, 3, 9, 1], 2), 7)


if __name__ == '__main__':
    unittest.main()
