import sys,os
sys.path.append(os.getcwd())
from base.Page import Page
from base.get_driver import get_driver
import pytest

def data():
    return [("1","休眠"),("2","移动网络"),("c","壁纸")]
class Test_one:

    def setup_class(self):
        self.driver = get_driver("com.android.settings",".Settings")

        self.page_obj=Page(self.driver)

    def teardown_class(self):
        self.driver.quit()
    @pytest.fixture(scope="class",autouse=True)
    def click_search(self):
        self.page_obj.click_search().search()
    @pytest.mark.parametrize("text,ve",data())
    def test_search(self,text,ve):
        self.page_obj.text_input().input_text(text)
        assert ve in self.page_obj.text_input().gain_text()



