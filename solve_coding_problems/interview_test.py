import unittest
from solve_coding_problems.google_interview_question import try_unsorted_pair_sum


class PairSumTests(unittest.TestCase):
    """check False result"""
    def test_false_result(self):
        self.assertFalse(try_unsorted_pair_sum([1, 2, 3, 9], 8),
                         "we should get False, because we don't have needed pair")

    def test_true_result(self):
        """check True result"""
        self.assertTrue(try_unsorted_pair_sum([1, 2, 4, 4], 8),
                        "we should get True, because we have needed pair")

    def test_wrong_types(self):
        """check wrong inputs"""
        self.assertEqual(try_unsorted_pair_sum([None], 2), "Exactly array and number required")


if __name__ == "__main__":
    unittest.main()
