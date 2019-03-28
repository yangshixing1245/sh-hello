from page.search_click import Search_click
from page.input_text import Input_Text

class Page:

    def __init__(self,driver):
        self.driver=driver
    def click_search(self):
        return Search_click(self.driver)
    def text_input(self):
        return Input_Text(self.driver)