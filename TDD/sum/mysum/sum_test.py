
import unittest

from mysum import my_sum


class MySumTests(unittest.TestCase):

	def setUp(self):
		# setting up
		self.numbers = [10,"5",78,90,60]

	def test_sum_of_digits(self):
		'''
		Test sum of digits or numbers
		'''
		result = my_sum(5,10)
		self.assertEqual(result, 15)
		self.assertEqual(my_sum(10, 15), 25)
		self.assertEqual(my_sum(78, 90), 168)
		self.assertEqual(my_sum(60, 15), 75)
		self.assertEqual(my_sum(70, 10), 80)
		self.assertEqual(my_sum(5, 15), 20)
		self.assertEqual(my_sum(10, 90),100)
		

	def test_non_numbers(self):
		'''
		Assert throwing of exception when it's a non-numbers
		'''
		
		self.assertEqual(my_sum(2, "5"), "Invalid input")
		
		

	def test_list(self):
		'''
		test if it receives an error since one is a list and another is a integer

		'''
		self.assertEqual(my_sum([70, 10], 7), "Invalid input")

		# with self.assertRaises(TypeError):
		# 	my_sum([2,5,7], 5)



if __name__ == '__main__':
	unittest.main()
