from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

numeroTiwtters = 5
tiwtterNivel = 3
elementosNuevos = False
listaTiwtter = []

driver = webdriver.Chrome(executable_path=r"D:\DriverChrome\chromedriver.exe")
driver.maximize_window()
driver.get("https://twitter.com/AnaPao_LePew")

#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article
#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[3]/div/div/article
#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[4]/div/div/article

time.sleep(3)

for i in range(numeroTiwtters):
    while elementosNuevos is not True:
        try:
            articulo = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div['+str(tiwtterNivel)+']/div/div/article')
            elementosNuevos = True
        except :
            driver.execute_script("window.scrollTo(0, 500)") 
    
    elementosNuevos = False

    textoPartido = articulo.text.split('\n')
    listaTiwtter+=[textoPartido]
    tiwtterNivel+=1

time.sleep(3)
driver.close()

print("Se obtuvieron un total de:"+str(len(listaTiwtter)))
print("Los cuales son:")
print(listaTiwtter)

# for articulo in articulos:
#     print(articulo.text)
#     textoPartido = articulo.text.split('\n')
#     #Tweet fijado
#     if 'Tweet fijado' not in textoPartido[0]:
#         print(textoPartido)
        
