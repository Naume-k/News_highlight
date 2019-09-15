import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources(1234,'A thrilling new Python Series','/khsjha27hbs',8.5,129993,'ffffffffffff','date')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))
   
if __name__ == '__main__':
    unittest.main()     