from time import sleep

from selenium.webdriver.common.by import By

from HomeWork.page.base_page import BasePage
#from HomeWork.page.contract import Contract
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Main(BasePage):
    _base_url="https://work.weixin.qq.com/wework_admin/frame#index"
    def download(self):
        pass

    def import_user(self, path):
        sleep(2)
        import_locator = "//span[contains(text(),'导入通讯录')]"
        self._driver.find_element(By.XPATH, import_locator).click()
        # self._driver.find_element(By.CSS_SELECTOR, "span:contains('导入通讯录')").click()  会报错不知道原因
        sleep(2)
        self._driver.find_element(By.ID, "js_upload_file_input").send_keys(path)
        self._driver.find_element(By.ID, "submit_csv").click()
        self._driver.find_element(By.ID, "reloadContact").click()
        return self

    def goto_app(self):
        pass

    def goto_managetool(self):
        self.find(By.CSS_SELECTOR, "span:contains('管理工具')").click()
        self.find(By.CSS_SELECTOR, "div:contains('素材库')").click()
        WebDriverWait(self._driver, 20, 0.5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span:contains('添加文字')")))
        
        return self

    def get_message(self):
        return ["aaa", "bbb"]

    def add_member(self):
        # self.find((By.LINK_TEXT, "添加成员")).click()
        # Chrome常见的问题，当click失败或无法用原生办法click时可使用js方式去执行
        self._driver.execute_script("argument[0].click", self.find((By.LINK_TEXT, "添加成员")))
        return Contract(reuse=True)
