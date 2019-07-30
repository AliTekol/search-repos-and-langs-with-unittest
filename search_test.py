import unittest
from search import *
import requests

class SearchTest(unittest.TestCase): 
    def test(self):   

        
        status_code_of_function = github_search("arduino", "python")
        self.assertEqual(status_code_of_function,200)

if __name__ == '__main__':
    unittest.main()