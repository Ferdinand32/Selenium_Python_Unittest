from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys 
import time 
import unittest



class FirstTetsSuit(unittest.TestCase):
    

    def setUp(self): 
        options = Options() 
        options.add_argument("--headless")
        self.page = webdriver.Chrome(chrome_options=options, executable_path='c:/cygwin64/home/_ADMIN_/Python/chromedriver')
        self.page.set_window_size(1200, 800) 

       
   
    def test_odin(self): 
        page = self.page 
        page.get("http://google.com") 
        page.save_screenshot("c:/cygwin64/home/_ADMIN_/Python/screenshot5.png") 
        
        
    def test_crif (self):
        page = self.page
        page.get("http://someSiteWithLogin")
        time.sleep(5) 
        page.save_screenshot("c:/cygwin64/home/_ADMIN_/Python/screenshot4.png") 
        result = page.find_element_by_xpath('/html/body/app-root/app-login/div/div/div[1]/div[2]/p')
        self.assertEqual(result.text, "Please, authenticate")
        #assert "Please, authenticate" in result.text

    def tearDown(self):
        self.page.close()
         

if __name__ == '__main__':
    unittest.main()

    