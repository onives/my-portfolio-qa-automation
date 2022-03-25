from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pdb
import time
import unittest


class MyPortfolioTestScript(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get("https://nameere-olive-nives.netlify.app/")

    # verify the projects are displayed on the projects page
    def test_projects_page(self):
        # verify the url of the page
        current_url = self.driver.current_url
        expected_url = "https://nameere-olive-nives.netlify.app/"
        self.assertEqual(expected_url, current_url, f"Got wrong site url. Current url: {current_url}")

        # navigate to the projects page
        projects_button_locator = '//*[@id="responsive-navbar-nav"]/div/a[2]'
        projects_element = self.driver.find_element(By.XPATH, projects_button_locator)
        projects_element.click()

        # verify the url of the current page
        expected_url = "https://nameere-olive-nives.netlify.app/projects"
        current_url = self.driver.current_url
        self.assertEqual(expected_url, current_url, f"Got wrong site url. Current url : {current_url}")

        # identify project element by xpath
        # verify its displayed
        # pdb.set_trace()

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
