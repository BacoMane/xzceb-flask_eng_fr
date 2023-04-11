import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when hello
        #self.assertEqual(english_to_french(''), null)  # test when null

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when bonjour 
        self.assertEqual(french_to_english(), null) # test when null.
        
unittest.main()