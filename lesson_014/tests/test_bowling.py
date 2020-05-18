import unittest
from bowling import get_score


class GetScoreTest(unittest.TestCase):

    def test_normal(self):
        result = get_score('45176181212171614181')
        self.assertEqual(result, 68)

    def test_spares(self):
        result = get_score('-/1/2/3/4/5/6/7/8/9/')
        self.assertEqual(result, 150)

    def test_strikes(self):
        result = get_score('XXXXXXXXXX')
        self.assertEqual(result, 200)

    def test_null(self):
        result = get_score('--------------------')
        self.assertEqual(result, 0)

    def test_mixed(self):
        result = get_score('185/X--26X-/X349/')
        self.assertEqual(result, 129)

    def test_too_many_pins(self):
        self.assertRaises(ValueError, get_score, '55-/8/8/34X8/5/1854')

    def test_second_throw_strike(self):
        self.assertRaises(ValueError, get_score, '1X18/8/34X8/5/1854')

    def test_zeroes_in_input(self):
        self.assertRaises(ValueError, get_score, '011/8/34X8/5/185412')

    def test_first_throw_spare(self):
        self.assertRaises(ValueError, get_score, '/11/8/34X8/5/185412')

    def test_not_ten_frames(self):
        self.assertRaises(ValueError, get_score, '-/8/8/34X8/5/1854')

    def test_input_error(self):
        self.assertRaises(ValueError, get_score, 'zzzzzzzzzzzzzzzzzzzz')


if __name__ == '__main__':
    unittest.main()
