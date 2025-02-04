
import unittest

from app.models import Article

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles(1234,'Python Must Be Crazy','A thrilling new Python Series','/khsjha27hbs',8.5,129993,'ffffffffffff','date')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

if __name__ == '__main__':
    unittest.main()