from selenium.webdriver.common.by import By


class UiElement:
    # 点击搜索
    search_id=(By.ID,"com.android.settings:id/search")
    # 文本输入框
    search_box_id =(By.ID,"com.android.settings:id/search")
    # 判断输入列表内容
    search_text_id = (By.ID,"com.android.settings:id/title")