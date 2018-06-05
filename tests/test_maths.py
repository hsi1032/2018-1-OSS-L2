from algorithms.maths import (
    combination,
    fibonacci,
    permutation,
    
)

import unittest
    
class TestSuite(unittest, Testcase):
  def test_combination(self):
    self.assertEqual(35, combination(7,3))
  def test_fibonacci(self):
    self.fibonacci(55, fibonacci(10))
  def test_permutation(self):
    self.assertEqual(210, permutation(7,3))
 
if __name__ == "__main__":
  unittest.main()
  
