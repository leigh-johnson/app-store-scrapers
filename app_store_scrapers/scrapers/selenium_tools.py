from selenium import webdriver

class AppleSearchAdsCookie():
    
    def __init__():
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.client = webdriver.Chrome(chrome_options=options)


    def tear_down(self):
        self.client.close()
