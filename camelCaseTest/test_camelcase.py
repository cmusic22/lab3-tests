import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):
	
	def test_camelCase_sentence(self):

		self.assertEqual('helloWorld', camelCase.camelcase('Hello World'))
		self.assertEqual('', camelCase.camelcase(''))
		self.assertEqual('helloWorld', camelCase.camelcase('    HELLO    WORLD   '))
		self.assertEqual('helloWorld1', camelCase.camelcase('Hello World 1'))
		self.assertEqual('helloWorld', camelCase.camelcase('Hello, worlD'))
		self.assertEqual('hello', camelCase.camelcase('Hello'))
		self.assertEqual('😀😁😂🤣😃😄😅😆😉', camelCase.camelcase('😀 😁 😂 🤣 😃 😄 😅 😆 😉'))

	