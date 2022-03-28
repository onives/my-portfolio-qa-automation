from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pdb
import time
import unittest


class MyProjectsPageTest(unittest.TestCase):

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
        projects_button_elem = self.driver.find_element(By.XPATH, projects_button_locator)
        projects_button_elem.click()

        # verify the url of the current page
        expected_url = "https://nameere-olive-nives.netlify.app/projects"
        current_url = self.driver.current_url
        self.assertEqual(expected_url, current_url, f"Got wrong site url. Current url : {current_url}")

        # verify project element is displayed
        project_locator_xpath = '//*[@id="root"]/div/div[1]/div[2]/div/div[1]'
        try:
            project_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, project_locator_xpath))
            )
            self.assertTrue(project_element.is_displayed())
        finally:
            pass
        # pdb.set_trace()

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
