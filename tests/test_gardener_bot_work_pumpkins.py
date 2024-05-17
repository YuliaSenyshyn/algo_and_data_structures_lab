import unittest

from src.gardener_bot_work_pumpkins import gardener_bot_work


class TestGardenerBotWork(unittest.TestCase):

    def test_equal_m_n_5(self):
        our_list = [[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25]]
        expected_output = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6, 11, 12, 13, 14, 15, 20, 19, 18, 17, 16, 21, 22, 23, 24, 25]
        self.assertEqual(gardener_bot_work(our_list), expected_output)

    def test_m_2_n_4(self):
        our_list = [[1, 2, 3, 4],
                    [5, 6, 7, 8]]
        expected_output = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(gardener_bot_work(our_list), expected_output)

    def test_n_1(self):
        our_list = [[1]]
        expected_output = [1]
        self.assertEqual(gardener_bot_work(our_list), expected_output)

    def test_m_6(self):
        our_list = [[1], [2], [3], [4], [5], [6]]
        expected_output = [1, 2, 3, 4, 5, 6]
        self.assertEqual(gardener_bot_work(our_list), expected_output)



if __name__ == '__main__':
    unittest.main()
