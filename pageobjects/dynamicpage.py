from selenium.webdriver.common.by import By
from pageobjects.locator import Locator


class Dynamic(object):
    def __init__(self, driver):
        self.driver = driver
        self.text = driver.find_elements(By.CSS_SELECTOR, Locator.dynamic_text_list)
        self.image = driver.find_elements(By.CSS_SELECTOR, Locator.dynamic_img_list)

    def get_dynamic_text_list(self):
        return self.text

    def get_dynamic_image_list(self):
        return self.image

    # common function  to retreive the longest string
    def get_longest_word(self, word, longest):
        w = word.rstrip()
        if len(w) >= 10 and len(w) > len(longest):
            longest = w
            print(len(w))
        print(longest)
        return longest

