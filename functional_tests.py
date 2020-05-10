from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        # user check out homepage
        self.browser.get('http://localhost:8020')

        # user checkout page title 
        self.assertIn('To-Do', self.browser.title)
        self.fail('test finished!')
        
        # other flows
        
if __name__ == '__main__':
    unittest.main(warnings='ignore')