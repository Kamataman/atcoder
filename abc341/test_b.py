import unittest
import b as target

class MyTest(unittest.TestCase):
    def test_ex1(self):
        n=4
        a=[5,7,0,3]
        s=[2,4,5]
        t=[2,3,2]
        expect=5
        result=target.function(n,a,s,t)
        self.assertEqual(result,expect)
    def test_ex2(self):
        n=10
        a=[32,6,46,9,37,8,33,14,31,5]
        s=[5,3,4,2,3,3,4,3,3]
        t=[5,1,3,2,2,2,4,3,1]
        expect=45
        result=target.function(n,a,s,t)
        self.assertEqual(result,expect)

if __name__ == '__main__':
    unittest.main()
