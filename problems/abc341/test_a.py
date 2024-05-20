import unittest
import a

class MyTest(unittest.TestCase):
    def test_ex1(self):
        n=4
        expect="101010101"
        result=a.funcA(n)
        self.assertEqual(result,expect)
    def test_ex2(self):
        n=1
        expect="101"
        result=a.funcA(n)
        self.assertEqual(result,expect)
    def test_ex3(self):
        n=10
        expect="101010101010101010101"
        result=a.funcA(n)
        self.assertEqual(result,expect)

if __name__ == '__main__':
    unittest.main()
