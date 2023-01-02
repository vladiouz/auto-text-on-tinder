from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

s = Service(r'C:\Users\Administrator\Desktop\cursuri\Udemy 100 Days of Python\chromedriver_win32\chromedriver.exe')
email = 'your-email'
password = 'your-password'
msg = 'your-msg'

driver = webdriver.Chrome(service=s)
driver.get('https://tinder.com/')
driver.maximize_window()

sleep(2)

login_button = \
    driver.find_element(By.XPATH,
                        '//*[@id="u-320325879"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

sleep(2)

login_with_fb = driver.find_element(By.XPATH,
                                    '//*[@id="u-2048706955"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
login_with_fb.click()

sleep(2)

tinder_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)

sleep(2)

allow_cookies = driver.find_elements(By.TAG_NAME, 'button')[-1]
allow_cookies.click()

sleep(2)

email_input = driver.find_element(By.ID, 'email')
email_input.send_keys(email)

password_input = driver.find_element(By.ID, 'pass')
password_input.send_keys(password)

sleep(2)

fb_login = driver.find_element(By.NAME, 'login')
fb_login.click()

sleep(10)

driver.switch_to.window(tinder_window)

allow_location = driver.find_element(By.XPATH, '//*[@id="u-2048706955"]/main/div/div/div/div[3]/button[1]')
allow_location.click()

sleep(2)

decline_notif = driver.find_element(By.XPATH, '//*[@id="u-2048706955"]/main/div/div/div/div[3]/button[2]')
decline_notif.click()

sleep(2)

accept_button = driver.find_element(By.XPATH, '//*[@id="u-320325879"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_button.click()

sleep(2)

slide_in_dm = driver.find_element(By.XPATH, '//*[@id="u-973122479"]/div[1]/div[2]/a')
slide_in_dm.click()

sleep(2)

text_area = driver.find_element(By.TAG_NAME, 'textarea')
text_area.send_keys(msg)

sleep(1)

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
