import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour', "The result should Bonjour") # test when hello
        self.assertIsNone(english_to_french(''), "The result should be null")  # test when null

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello', "The result should be Hello") # test when bonjour 
        self.assertIsNone(french_to_english(''), "The result should be nnull") # test when null.
        
unittest.main()