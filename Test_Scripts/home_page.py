from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pdb
import time
import unittest
import pdb


class MyPortfolioTestScript(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("https://nameere-olive-nives.netlify.app/")

    # verify the title of the page
    def test_title(self):

        # verify the title of the page
        current_title = self.driver.title
        expected_title = "Nameere Olive Nives"
        self.assertEqual(expected_title, current_title, f"Got wrong title. Current title: {self.driver.title}")

        # verify the url of the page
        current_url = self.driver.current_url
        expected_url = "https://nameere-olive-nives.netlify.app/"
        self.assertEqual(expected_url, current_url, f"Got wrong site url. Current url: {current_url}")

        # verify the content of the bio section of the home-page is displayed
        bio_link_locator = "#root > div > div.container-div > div.bio-div > p"
        bio_element = self.driver.find_element(By.CSS_SELECTOR, bio_link_locator)
        # wait a few seconds before checking since bio api takes long to load on browser
        time.sleep(2)
        self.assertTrue(bio_element.is_displayed())

        # pdb.set_trace()
        # time.sleep(5)
    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
