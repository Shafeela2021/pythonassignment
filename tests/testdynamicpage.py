import pytest
from selenium import webdriver
from pageobjects.dynamicpage import Dynamic
import os
import configparser

# Reading the config file from resources folder
os.chdir(os.path.dirname(__file__))
os.chdir('..')
dirPath = os.getcwd()
file_path = os.path.join(dirPath, 'resources')
file_name = os.path.join(file_path, 'page-config.ini')
config = configparser.ConfigParser()
config.read(file_name)


class TestHerokuapp:

    def setup_class(self):
        print("setting up  the environment")
        self.driver = webdriver.Chrome()
        self.url = config.get('dynamic_page', 'url')
        print(self.url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def teardown_class(self):
        if self.driver is not None:
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()

    @pytest.mark.parametrize("expected_length", [10])
    def test_dynamic_text(self, expected_length):
        dynamic = Dynamic(self.driver)
        elm = dynamic.get_dynamic_text_list()
        i = 1
        longest = ''
        while i < len(elm):
            words = elm[i].text
            longest = self.get_longest_word(words, longest)
            i += 1
        assert len(longest) >= expected_length

    @pytest.mark.parametrize("invalid_img", ['3'])
    def test_dynamic_image(self, invalid_img):
        dynamic = Dynamic(self.driver)
        imgs = dynamic.get_dynamic_image_list()
        for img in imgs:
            img_url = img.get_attribute('src')
            avatar_id = ''.join(filter(str.isdigit, img_url))
            if len(avatar_id) == 1:
                print("Avatar id is {}, name {}".format(avatar_id, self.get_avatar_name(avatar_id)))
                if invalid_img is avatar_id:
                    print('punisher found')
                    assert False
        assert True

    @classmethod
    def get_avatar_name(cls, avatar_id):
        dic = {'1': 'Mario', '2': 'Mandalorian', '3': 'Punisher', '5': 'Wolverine', '6': 'Storm Trooper', '7': 'Joker'}
        return dic[avatar_id]

    @classmethod
    def get_longest_word(cls, words, longest):
        # print(words)
        for word in words.split(' '):
            if len(word) >= 10 and len(word) > len(longest):
                longest = word
        print(len(longest))
        print(longest)
        return longest
