from selenium import webdriver
from shutil import which
import time
from PIL import Image

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from lxml import etree

from selenium_stealth import stealth
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import undetected_chromedriver.v2 as uc

driver = uc.Chrome()
chrome_options = uc.ChromeOptions()

cap = DesiredCapabilities().CHROME

chrome_path = which("./chromedriver")

# chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1420,1080")
# chrome_options.add_argument('allow-elevated-browser')
# chrome_options.add_argument(f"user-agent={user_agent}")

# driver = webdriver.Chrome(executable_path=chrome_path,options=chrome_options,desired_capabilities=cap)

# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )

cap = DesiredCapabilities().FIREFOX

path = "./geckodriver"
options = Options()
options.add_argument("--headless")

# driver = webdriver.Firefox(executable_path = path,options=options)

url = 'https://www.youtube.com/channel/UCMGe647gY0RENASDZ1CrXQQ/videos'
# driver.get(url)
with driver:
        driver.get(url)

driver.implicitly_wait(5)

Html_Source =  driver.page_source
tree = etree.HTML(Html_Source)
video = tree.xpath('//a[@id="video-title" and @href]/@href')
Channel_Name = tree.xpath('(//yt-formatted-string[@class="style-scope ytd-channel-name"]/text())[21]')
print(Channel_Name)
# video = driver.find_element_by_xpath('//a[@id="video-title" and @href]')
for elem in video:
        A = 'https://youtube.com' + elem
        # print(type(A))
        with driver:
                driver.get(A)
        Html_Source =  driver.page_source
        tree = etree.HTML(Html_Source)
        video_name = tree.xpath('(//yt-formatted-string[@class="style-scope ytd-video-primary-info-renderer"])[1]/text()')
        video_date = tree.xpath('(//yt-formatted-string[@class="style-scope ytd-video-primary-info-renderer"])[2]/text()')
        video_description = tree.xpath('//div[@id="description"]/*/span/text()')

        string_to_break = '\nWatch' # the 2021 Berkshire Hathaway Annual Shareholders Meeting on YouTube:'

        # video_description = video_description.split(string_to_break)[0]
        video_description_split = [i.split('\nWatch') for i in video_description]
        # print(type(video_description))
        print(video_name)
        print(video_date)
        print(video_description_split)

#     print(elem.get_attribute("href"))
# video.click()



# time.sleep(20)

# driver.implicitly_wait(102)

# file_name = 'After.png'
# driver.save_screenshot(file_name)
# image = Image.open(file_name)
# image.show()
driver.close()
driver.quit()
