import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # Test for the translation of the world 'Hello' and 'Bonjour'.

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # Test for the translation of the world 'Hello' and 'Bonjour'.
        
unittest.main()
