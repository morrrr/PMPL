from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):

	def test_bad_maths(self):
		self.asserEqual(1+1,3)
