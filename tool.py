from selenium.webdriver.common.by import By
from HomeWork.page.materials import Materials

from HomeWork.page.base_page import BasePage


class ManageTool(BasePage):
    _base_url="https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def add_member(self):
        pass

    def sync_contact(self):
        pass

    def group_message(self):
        pass

    def add_materials(self):
        self.find(By.CSS_SELECTOR, "li div div:contains('素材库')").click()
        # self.find(By.XPATH, "//div[contains(text(), '素材库')]").click()
        return Materials(reuse=True)
