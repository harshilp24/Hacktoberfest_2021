from selenium import webdriver
import selenium

product = input("Enter the URL of the product: ")   # Takes URL of the product as the input from the user

driver=webdriver.Chrome()

driver.get(product)
try:
    price = driver.find_element_by_xpath('//*[@id="priceblock_dealprice"]').text           # Checks if there is an offer price
except:
    price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text            # Gives the normal price if there are no offers

file = open('prices.txt','a',encoding='utf-8')                                             # Stores the prices in a text file
file.write(price+'\n')
file.close()
