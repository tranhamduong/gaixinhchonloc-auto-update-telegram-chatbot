from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.firefox.options import Options
import os

from time import sleep

first_index = 4
url = 'https://t.me/s/gaixinhchonloc/'
image_url = 'https://t.me/gaixinhchonloc/'

opts = Options()
# opts.headless = True
opts.set_preference('dom.webnotifications.enabled', False)
opts.set_preference('dom.push.enabled', False)

driver = webdriver.Firefox(options=opts)



def first_run():
    print('this is first run')
    
    last_index = get_last_image_index()
    print(last_index)
    
    
    for index in range(last_index, first_index, -1):
        index_url = image_url + str(index)
        print('Get image from ' + index_url)
        try:
            temp_driver = webdriver.Firefox(options=opts)
            temp_driver.get(index_url)
            
            image_style = temp_driver.find_elements_by_class_name('tgme_widget_message_photo_wrap')
            
            print(image_style)
            
            
            
            temp_driver.close()
        except InvalidArgumentException:
            print(index_url)
        
        
    
    
    
def daily_run():
    print('this is daily run')
    
def init():
    try:
        driver.get(url)
    except InvalidArgumentException:
        print(url)
    
def get_last_image_index():
    list_image = driver.find_elements_by_class_name('tgme_widget_message_photo_wrap')
    last_image_index = list_image[-1].get_attribute('href').split('/')[-1]
    
    return int(last_image_index)
    
    

def main():
    print('this is main')
if __name__ == '__main__':
    init()
    first_run()
    