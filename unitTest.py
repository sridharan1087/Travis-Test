import unittest
from firstCode import name


class TestfirstCode(unittest.TestCase):
    def test_name(self):
        self.assertIsInstance(name('ajay'),str)
        
        
        
if __name__ == '__main__':
#    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestfirstCode)
    unittest.TextTestRunner(verbosity=2).run(suite)