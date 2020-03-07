from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#把初始化放在一个Page里，其他Page可以继承该类共用此方法
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ""
    # _driver = None
    def __init__(self, driver: WebDriver=None, reuse=False):

        if driver is None:
            if reuse:
                chromeoptions = Options()
                '''
                使用已打开的chrome浏览器绕过验证
                --打开windows cmd 进入chrome安装目录，一般在C:\Program Files (x86)\Google\Chrome\Application下，然后运行
                chrome.exe --remote-debugging-port=9222
                '''
                chromeoptions.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                self._driver = webdriver.Chrome(chrome_options=chromeoptions)
            else:
                # index页面会使用这个
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)

        # 给不需要重新启动浏览器的page使用, Login与Register等页面需要用这个方法
        else:
            self._driver = driver

        if self._base_url !="":
            # 加入self._base_url可以让每个page定义自己需要打开的地址
            self._driver.get(self._base_url)

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def close(self):
        sleep(20)
        self._driver.quit()