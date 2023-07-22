
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Add item to cart from home page to verify coupon
driver = webdriver.Chrome()
url1 = 'http://127.0.0.1:8888/mysite2/'
driver.get(url1)

product_name = driver.find_element(By.XPATH, '//*[@id="main"]/ul/li[2]/a[1]/img')
add_item_to_cart = driver.find_element(By.CSS_SELECTOR, '#main > ul > li.product.type-product.post-18.status-publish.instock.product_cat-accessories.has-post-thumbnail.sale.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
add_item_to_cart.click()
driver.implicitly_wait(5)
view_cart = driver.find_element(By.CSS_SELECTOR, '#main > ul > li.product.type-product.post-18.status-publish.instock.product_cat-accessories.has-post-thumbnail.sale.shipping-taxable.purchasable.product-type-simple > a.added_to_cart.wc-forward')
view_cart.click()

# verify apply coupon by adding invalid coupon

coupon_input = driver.find_element(By.ID, 'coupon_code')
coupon_input.send_keys('invalid coupon')

apply_coupon = driver.find_element(By.CSS_SELECTOR, '#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button')
apply_coupon.click()
driver.implicitly_wait(5)

# Wait for the error message to appear
error_message = driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul/li')
display_error = error_message.text


import pdb; pdb.set_trace()
