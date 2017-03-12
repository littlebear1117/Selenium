
# Alex helped to create this by searching on the web
# Create a simple web drive to open chrome and make a simple search.

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
# from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import unittest

class GoogleTest(unittest.TestCase):

 # def test_google_search(self):
 #    # Create a new instance of the Firefox driver
 #    driver = webdriver.Firefox()
 #
 #    # go to the google home page
 #    driver.get("http://www.google.com")
 #
 #    # the page is ajaxy so the title is originally this:
 #    print driver.title
 #
 #    # find the element that's name attribute is q (the google search box)
 #    inputElement = driver.find_element_by_name("q")
 #
 #    # type in the search
 #    inputElement.send_keys("cheese!")
 #
 #    # submit the form (although google automatically searches now without submitting)
 #    inputElement.submit()
 #
 #    try:
 #        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
 #        WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
 #
 #        # You should see "cheese! - Google Search"
 #        print driver.title
 #
 #    finally:
 #        driver.quit()

  def test_calculator(self):
      assert calculator.add(5,7) == 12





#suite = unittest.TestLoader().loadTestsFromTestCase(GoogleTest)
#unittest.TextTestRunner(verbosity=2).run(suite)

