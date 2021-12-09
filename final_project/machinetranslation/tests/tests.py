"""Testing file"""
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    '''The test class for translate english to french'''
    def test1(self):
        '''The test function for Hello is equal to Bonjour'''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test2(self):
        '''The test function for Hello is not equal to Hello'''
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TestFrenchToEnglish(unittest.TestCase):
    '''The test class for translate english to french'''
    def test1(self):
        '''The test function for Bonjour is equal to Hello'''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test2(self):
        '''The test function for Bonjour is not equal to Bonjour'''
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()
