import unittest
import csv
import time
import json
from selenium import webdriver

__author__ = 'Kan!skA'


class RESTClient(unittest.TestCase):
    driver = None

    def setUp(self):
        # For Mac/Linux, you've to change this Profile Location.
        profile = webdriver.FirefoxProfile(
            "C:/Users/kaniskan/AppData/Roaming/Mozilla/Firefox/Profiles/rmnuc28u.default")
        self.driver = webdriver.Firefox(profile)
        self.driver.maximize_window()
        self.driver.get("chrome://restclient/content/restclient.html")

    def test_URL(self):
        # Read the CSV File
        data_file = open("input.csv", "r")
        read = csv.reader(data_file)
        line = 0
        for row in read:
            line += 1
            self.driver.implicitly_wait(5)
            wservice = "http://10.208.11.96:8080/transformer.gistconnect.in/segments?passkey=051def518d82001232c05afcc128ba6a&url="
            self.driver.find_element_by_xpath("html/body/div[1]/div/div/div/ul[1]/li[3]/a").click()
            self.driver.find_element_by_xpath("html/body/div[1]/div/div/div/ul[1]/li[3]/ul/li[3]/a").click()
            self.driver.find_element_by_xpath(".//*[@id='request-form']/form/span[1]/a/i").click()
            self.driver.find_element_by_xpath(".//*[@id='request-method-list']/li[2]/a").click()
            self.driver.find_element_by_xpath(".//*[@id='request-url']").send_keys(wservice+wservice.join(row))
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath(".//*[@id='request-button']").click()
            time.sleep(11)
            self.driver.find_element_by_xpath(".//*[@id='response-tabs']/li[2]/a").click()
            time.sleep(5)
            # For Mac/Linux, Change your preferred location.
            loc = "F:\\" + str(line) + ".txt"
            with open(loc, 'w', encoding="utf-8") as f:
                f.write(wservice.join(row)+"\n")
                temp = self.driver.find_element_by_xpath(".//*[@id='response-body-raw']/pre").text
                data = json.loads(temp)
                f.write(data['op_segment'])
            time.sleep(2)
            self.driver.refresh()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
