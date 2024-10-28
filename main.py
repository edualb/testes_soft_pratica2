import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUI(unittest.TestCase):

    def setUp(self):
        # É necessário especificar o geckdriver do snap no Ubuntu 24.04
        # https://github.com/mozilla/geckodriver/issues/2010
        service = Service(executable_path="/snap/bin/firefox.geckodriver")
        self.driver = webdriver.Firefox(service=service)

    def test_success(self):
        try:
            file_path = os.path.abspath("sample-exercise.html")
            self.driver.get("file://" + file_path)

            button_generate = self.driver.find_element(by=By.NAME, value="generate")
            button_generate.click()
            
            generate_output = self.driver.find_element(by=By.ID, value="my-value")
            WebDriverWait(self.driver, 10).until(
                lambda _: generate_output.text != ""
            )
            
            input = self.driver.find_element(by=By.ID, value="input")
            input.clear()
            input.send_keys(generate_output.text)
            WebDriverWait(self.driver, 10).until(
                lambda _: input.get_attribute("value") == generate_output.text
            )

            button_test = self.driver.find_element(by=By.NAME, value="button")
            button_test.click()

            WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # "dummy" sleep para ver que o alert está sendo exibido
            time.sleep(1)
            
            alert = self.driver.switch_to.alert
            alert.dismiss()

            result_output = self.driver.find_element(by=By.ID, value="result")
            WebDriverWait(self.driver, 10).until(
                lambda _: result_output.text != ""
            )

            self.assertEqual(result_output.text, f"It workls! {generate_output.text}!")

            # "dummy" sleep para ter uma percepção humana do que está a acontecer na tela.
            time.sleep(1)
            
            self.driver.close()
        except Exception as e:
            self.fail(f"An error occurred: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()