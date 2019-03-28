from base.Base import Base
from page.UiElement import UiElement


class Input_Text(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)

    def input_text(self,text):
        self.send_element(UiElement.search_box_id,text)

    def gain_text(self):
        data=self.search_elements(UiElement.search_text_id)
        return [i.text for i in data]
