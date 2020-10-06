from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time
import os


class Amazon_Scraper:
    def __init__(self,  num_books,keyword, driver_path="./chromedriver.exe", slp_time=15, verbose=False):
        # self.keyword = keyword
        self.num_books = num_books
        self.driver_path = driver_path
        self.slp_time = slp_time
        self.verbose = verbose
        self.url = 'https://www.amazon.in/s?k= '+ keyword
        self.books = []

    def set_driver(self, url):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options._binary_location= os.environ.get("GOOGLE_CHROME_BIN")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=400,800")
        options.add_argument("--start-maximized")
        options.add_argument("--headless")

        driver = webdriver.Chrome(executable_path=self.driver_path, options=options)
        driver.set_window_size(1120, 1000)
        driver.get(url)

        return driver

    def get_books(self):
        driver = self.set_driver(url=self.url)
        while len(self.books) < self.num_books:  # If true, should be still looking for new books.

            time.sleep(self.slp_time)

            # book_links = driver.find_elements_by_class_name('a-link-normal')
            book_links = driver.find_elements_by_xpath("//a[@class='a-link-normal a-text-normal']")
            for book_link in book_links:
                final_url = book_link.get_attribute("href")
                print("Progress: {}".format("" + str(len(self.books)) + "/" + str(self.num_books)))
                self.get_book_details(url=final_url)
                if len(self.books) >= self.num_books:
                    break
            print("Go next Page")
            print('books')
            # Clicking on the "next page" button
            try:
                driver.find_element_by_xpath('.//li[@class="a-last"]//a').click()
            except NoSuchElementException:
                print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(
                    self.num_books, len(self.books)))
                break
        driver.close()
        # self.save_books_data()

        return self.books

    def get_book_details(self, url):
        book_details = {}
        driver = self.set_driver(url=url)
        time.sleep(2)
        book_details["title"] = driver.find_element_by_xpath("//span[@id='productTitle']").text
        try:
            book_details["image_src"] = driver.find_element_by_xpath("//div[@id='img-canvas'] //img").get_attribute("src")
        except NoSuchElementException:
            book_details["image_src"] = -1
        try:
            book_details["author"] = [e.text for e in driver.find_elements_by_xpath("//span[@class='author notFaded'] //a")]
        except NoSuchElementException:
            book_details["author"] = -1
        try:
            book_details["price"] = driver.find_element_by_xpath("//span[@class='a-size-base a-color-price a-color-price']").text
        except NoSuchElementException:
            book_details["price"] = -1

        # driver.switch_to.default_content()

        try:
            book_details["rating"] = driver.find_element_by_xpath("//span[@id='acrPopover']").get_attribute("title")
        except NoSuchElementException:
            book_details["rating"] = -1

        try:
            book_details["total_raters"] = driver.find_element_by_xpath("//span[@id='acrCustomerReviewText']").text
        except NoSuchElementException:
            book_details["total_raters"] = -1

        try:
            iframe = driver.find_element_by_xpath("//iframe[@id='bookDesc_iframe']")
            driver.switch_to.frame(iframe)
            book_details["description"] = driver.find_element_by_xpath("//div[@id='iframeContent']").get_attribute('innerHTML')
        except NoSuchElementException:
            book_details["description"] = -1

        driver.switch_to.default_content()

        try:
            driver.find_element_by_xpath("//div[@id='reviews-medley-footer']//a").click()
            # time.sleep(5)
            try:
                book_details["reviews"] = [e.get_attribute("innerHTML") for e in driver.find_elements_by_xpath("//span[@class='a-size-base review-text review-text-content'] / span ")]
            except NoSuchElementException:
                book_details["reviews"] = -1
        except NoSuchElementException:
            time.sleep(1)
            book_details["reviews"] = -1
        # book_details["book_review"]
        print(book_details)
        self.books.append(book_details)
        driver.close()

