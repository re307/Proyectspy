from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"D:\DriverChrome\chromedriver.exe")
driver.get("https://twitter.com/AnaPao_LePew")

#//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]
# driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/a[2]').click()
# time.sleep(5)
#name session[username_or_email]
# driver.find_element_by_name('session[username_or_email]').send_keys('EduardoSex307')
#name session[password]
# driver.find_element_by_name('session[password]').send_keys('pumas2018')
#//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div
# driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div').click()
# time.sleep(5)
#article
# articulos = driver.find_elements_by_tag_name("article")
#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article
#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/div/article
#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[4]/div/div/article

# for articulo in articulos:
#     # print(articulo.text)
#     textoPartido = articulo.text.split('\n')
#     #Tweet fijado
#     if 'Tweet fijado' not in textoPartido[0]:
#         print(textoPartido)
        
driver.close()
