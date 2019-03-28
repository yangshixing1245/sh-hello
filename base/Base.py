from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self,driver):
        self.driver = driver

    def search_element(self,loc,timeout=10,poll_frequency=1):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))

    def search_elements(self,loc,timeout=10,poll_frequency=1):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_elements(*loc))

    def click_element(self,loc,timeout=10,poll_frequency=1):
        self.search_element(loc,timeout,poll_frequency).click()
    def send_element(self,loc,text,timeout=10,poll_frequency=1):
        data=self.search_element(loc,timeout,poll_frequency)
        data.clear()
        data.send_keys(text)






