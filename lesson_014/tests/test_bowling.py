import unittest
from bowling import get_score


class GetScoreTest(unittest.TestCase):

    def test_normal(self):
        result = get_score('45106181900071619181')
        self.assertEqual(result, 69)

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
    # TODO Нужно ещё добавить тесты с ошибками
    # with self.assertRaises(ValueError):
    #     get_score(...)
    # TODO Для этого можно пользоваться подобной конструкцией

if __name__ == '__main__':
    unittest.main()
