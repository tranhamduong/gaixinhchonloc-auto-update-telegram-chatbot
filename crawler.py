from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.firefox.options import Options
import os
from selenium.webdriver.common.keys import Keys


from PIL import Image


import tinify
tinify.key = "X6gSRMJrj2s4gms24NmhgNshRX39G2qB"


from time import sleep

first_index = 4
url = 'https://t.me/s/gaixinhchonloc/'
image_url = 'https://t.me/gaixinhchonloc/'
post_image_url = '?embed=1'

# opts = Options()
# # sopts.headless = True
# opts.set_preference('dom.webnotifications.enabled', False)
# opts.set_preference('dom.push.enabled', False)
# opts.set_preference('dom.disable_beforeunload', True)



# # opts._binary_location = '/usr/local/bin/chromedriver'
# # opts.set_preference()

# driver = webdriver.Firefox(options = opts)
chrome_options= webdriver.ChromeOptions()
chrome_options.set_headless(True)

driver = webdriver.Chrome(chrome_options=chrome_options)

def first_run():
    print('this is first run')
    
    last_index = get_last_image_index()
    print(last_index)
    
    
    for index in range(last_index, first_index, -1):
        index_url = image_url + str(index) + post_image_url
        print('Get image from ' + index_url)
        try:
            temp_driver = webdriver.Chrome(chrome_options=chrome_options)
            temp_driver.get(index_url)
            
            try: 
                style_link = temp_driver.find_elements_by_class_name('tgme_widget_message_photo_wrap')[0]
                image_direct_index_str = str(style_link.get_attribute('style'))
                image_direct_index = image_direct_index_str.find('https://')
                image_direct_url = image_direct_index_str[int(image_direct_index): len(image_direct_index_str) -3]
                # print(image_direct_url)
                resize_image(image_direct_url, index)
                temp_driver.close()
            except IndexError:
                temp_driver.close()
                continue
        except InvalidArgumentException:
            print(index_url)
        
def resize_image(image_url, index):
    source = tinify.from_url(image_url)
    resized = source.resize(
        method="cover",
        width=512,
        height=512
    )
    output_name = 'img/output_' + str(index)
    resized.to_file(output_name + '.jpg')

    img = Image.open(output_name + '.jpg')
    img.save(output_name + '.png')

    os.remove(output_name + '.jpg')
    
def send_to_telegram(image_index):

    options = webdriver.ChromeOptions()
    options.add_argument('--profile-directory=Default')
    options.add_argument('--user-data-dir=/home/duongth/.config/google-chrome')
    
    # driver = webdriver.Chrome(options=options,executable_path='/usr/local/bin/chromedriver')
                              
    telegram =  webdriver.Chrome(chrome_options= options)
    telegram.get('https://web.telegram.org')
    
    sleep(5)
    telegram.find_elements_by_partial_link_text('Stickers')[0].click()
    # telegram.find_elements_by_css_selector('.composer_rich_textarea')[0].send_keys(os.getcwd() + '/img/output_672.png')
    # abc = telegram.find_element_by_css_selector('/composer_rich_textarea')
    
    #! droparea
    telegram.find_element_by_xpath("//input[@class='im_attach_input']").send_keys(os.getcwd() + '/img/output_672.png')
    #drop_area = telegram.find_elements_by_css_selector('.composer_rich_textarea')[0]
    

    # telegram.find_element_by_xpath("//button[@type='submit']").click()

    
    
    # send_button = telegram.find_elements_by_class_name('btn-md')[0]
    # send_button

    sleep(10)



    telegram.close()

    
    
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
    # init()
    #first_run()
    send_to_telegram(image_url)
    