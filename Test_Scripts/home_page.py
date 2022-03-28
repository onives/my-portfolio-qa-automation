from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb


class MyHomePageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("https://nameere-olive-nives.netlify.app/")

    # verify the homepage of the site
    def test_homepage(self):

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
        # Explicitly wait a few seconds before checking since bio api takes long to load on browser
        try:
            bio_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, bio_link_locator))
            )
            self.assertTrue(bio_element.is_displayed())
        finally:
            pass

        # pdb.set_trace()

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
