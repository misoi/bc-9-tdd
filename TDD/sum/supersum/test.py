import unittest
from super_sum import super_sum


class MySumTests(unittest.TestCase):

	def test_sum_of_inputs(self):
		'''
		Test sum of digits or numbers
		'''
		self.assertEqual(super_sum([78, 90,10], 178)
		self.assertEqual(super_sum(10,5,2), 17)		
		self.assertEqual(super_sum([60, 15], 6, 2), 83)
		self.assertEqual(super_sum([70, 10], [2,4]), 86)
		self.assertEqual(super_sum('me', 7), 'wrong input type')
		self.assertEqual(super_sum([10, 90], [5, 2], [4, 6]), 117)
	

if __name__ == '__main__':
	unittest.main()
