from selenium import webdriver
import unittest

class PageObjects(object):

    def searchField(self, driver):
        return  driver.find_element_by_name("q")

class AndrewTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print "Before ALL"

    @classmethod
    def tearDownClass(cls):
        print "After All"

    def setUp(self):
        print "before test case"

class GoogleTest(AndrewTests):
# Create a new Firefox webdriver

  def test_selenium(self):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    # driver.maximize_window()
    # navigate to the application home page
    driver.get("http://google.com/")
    # get the search textbox
    search_field = PageObjects.search_field(driver=driver)
    search_field.clear()
    # enter search keyword and submit
    search_field.send_keys("phones")
    search_field.submit()
    # get all the anchor elements which have product names displayed
    # currently on result page using find_elements_by_xpath method
    products = driver.find_elements_by_class_name("ads-ad")
    # get the number of anchor elements found
    print "Found " + str(len(products)) + " products:"
    # iterate through each anchor element and print the text that is
    # name of the product
    for product in products:
        print product.text
    # close the browser window
    # driver.quit()

  def test_selenium2(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        # driver.maximize_window()
        # navigate to the application home page
        driver.get("http://google.com/")
        # get the search textbox
        search_field = driver.find_element_by_name("q")
        search_field.clear()
        # enter search keyword and submit
        search_field.send_keys("phones")
        search_field.submit()
        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = driver.find_elements_by_class_name("ads-ad")
        # get the number of anchor elements found
        print "Found " + str(len(products)) + " products:"
        # iterate through each anchor element and print the text that is
        # name of the product
        for product in products:
            print product.text
        # close the browser window
        # driver.quit()

class GoogleTest2(AndrewTests):
# Create a new Firefox webdriver

  def test_selenium(self):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    # driver.maximize_window()
    # navigate to the application home page
    driver.get("http://google.com/")
    # get the search textbox
    search_field = driver.find_element_by_name("q")
    search_field.clear()
    # enter search keyword and submit
    search_field.send_keys("phones")
    search_field.submit()
    # get all the anchor elements which have product names displayed
    # currently on result page using find_elements_by_xpath method
    products = driver.find_elements_by_class_name("ads-ad")
    # get the number of anchor elements found
    print "Found " + str(len(products)) + " products:"
    # iterate through each anchor element and print the text that is
    # name of the product
    for product in products:
        print product.text
    # close the browser window
    # driver.quit()


# Command line: "python -m unittest searchproducts.GoogleTest"  --> This one failed with error
# And: "python -m unittest searchproducts.GoogleTest2"

# Reference:
# https://docs.python.org/2/library/unittest.html#setupclass-and-teardownclass
