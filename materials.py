from selenium.webdriver.common.by import By

from HomeWork.page.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Materials(BasePage):

    def add_word(self):
        pass

    def add_rich_txt(self):
        pass

    def add_image(self, data):
        WebDriverWait(self._driver, 20, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '图片')]")))
        self.find(By.XPATH, "//a[contains(text(), '图片')]").click()
        self.find(By.XPATH, "//a[contains(text(), '添加图片')]").click()
        self.find(By.ID, "js_upload_input").send_keys(data)
        self._driver.implicitly_wait(3)
        self.find(By.XPATH, "//a[contains(text(), '完成')]").click()
        # self._driver.execute_script("argument[0].click", self.find((By.XPATH, "//a[contains(text(), '完成')]")))

        return self


    def add_voice(self):
        pass