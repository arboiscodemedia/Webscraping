from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib
import urllib.request

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('log-level=3')
driver = webdriver.Chrome(executable_path=r'./driver/chromedriver.exe',options = options)
driver.get('https://www.nasa.gov/multimedia/imagegallery/iotd.html')
images = driver.find_elements_by_xpath('//div[@class="image"]/img')
count = 0
for image in images:
    print(image.get_attribute('src'))
    suffix = pathlib.Path(image.get_attribute('src')).suffix
    if suffix and suffix.strip():
        urllib.request.urlretrieve(image.get_attribute('src'),f"./images/search{count+1}{suffix}")
    count += 1
driver.close()    