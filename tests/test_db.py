import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_connect(self):
        from db import utils
        utils.show_tables()

if __name__ == '__main__':
    unittest.main()
