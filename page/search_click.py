from base.Base import Base
from page.UiElement import UiElement


class Search_click(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def search(self):
        self.click_element(UiElement.search_id)