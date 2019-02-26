from selenium import webdriver

driver=webdriver.chrome()
driver.get('https://web.whatsapp.com')

names = ['My No BSNL','My No Airtel']
msg = input('enter your message:')
count = int(input('enter the count : '))

input('enter anything after scanning qr code')

for name in names:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    
    msg_box = driver.find_element_by_class_name('_2SVIP')
    
    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('-35EW6')
        button.click()
