import unittest
from search import github_search

class SearchTest(unittest.TestCase): 
    def test(self):   
        output = github_search("arduino", "python") 
        num_lines = 0  
        for line in output:
            num_lines += 1
        print("Count of the sites :",num_lines)
        self.assertGreaterEqual(num_lines,1)

if __name__ == '__main__':
    unittest.main()