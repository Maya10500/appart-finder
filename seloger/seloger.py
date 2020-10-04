from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class Seloger(object):
    def __init__(self):
        options = Options()
        download_folder = "C:\\"

        profile = {"plugins.plugins_list": [{"enabled": False,
                                             "name": "Chrome PDF Viewer"}],
                   "download.default_directory": download_folder,
                   "download.extensions_to_open": ""}

        options.add_experimental_option("prefs", profile)
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        # Headless one :
        # driver = webdriver.Chrome(chrome_options=options)
        driver = webdriver.Chrome()
        self.driver =driver
    def get_url(self,url):
        self.driver.get(url)
    def do_research(self):
        location = self.driver.find_element_by_xpath('//*[@id="agatha_autocomplete_autocompleteUI__input"]')
        location.send_keys("Lyon")
    def click(self,element):
        button = self.driver.find_element_by_xpath(element)
        button.send_keys(Keys.ENTER)
    def enter_value(self,element,value):
        if type(value) is int:
            self.put_number(str(value),element)
        else:
            input = self.driver.find_elements_by_xpath(element)
            for i in input:
                i.send_keys(value)
    def get_all(self):
        elements = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]')
        for element in elements:
            print(element.text)
    def quit(self):
        self.driver.quit()

    def put_number(self, string_number,element):
        for _,value in enumerate(string_number):
            key = ""
            if value == "0":
                key = Keys.NUMPAD0
            if value == "1":
                key = Keys.NUMPAD1
            if value == "2":
                key = Keys.NUMPAD2
            if value == "3":
                key = Keys.NUMPAD3
            if value == "4":
                key = Keys.NUMPAD4
            if value == "5":
                key = Keys.NUMPAD5
            if value == "6":
                key = Keys.NUMPAD6
            if value == "7":
                key = Keys.NUMPAD7
            if value == "8":
                key = Keys.NUMPAD8
            if value == "9":
                key = Keys.NUMPAD9
            input = self.driver.find_element_by_xpath(element)
            input.send_keys(key)
