import unittest
from search import github_search

class SearchTest(unittest.TestCase): 
    def test(self):    
        output = github_search("arduino", "python")
        count = len(output)
        self.assertGreaterEqual(count,1)

if __name__ == '__main__':
    unittest.main()