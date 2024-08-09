from selenium import webdriver
from PIL import Image
import time

def HTB_screenshot(url, x, y, width, height, output_file):
    if os.path.exists(screenshot_file):
        os.remove(screenshot_file)
    if os.path.exists(output_file):
        os.remove(output_file)
    
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    driver.save_screenshot('profile.png')
    
    with Image.open('profile.png') as image:
        cropped_img = image.crop((x, y, x + width, y + height))
        cropped_img.save(output_file)
    driver.quit()

url = 'https://www.hackthebox.com/profile'
x, y, width, height = 100, 200, 800, 600
output_file = 'rank.png'

HTB_screenshot(url, x, y, width, height, output_file)
