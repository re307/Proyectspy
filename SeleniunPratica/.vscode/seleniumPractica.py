from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

numeroTiwtters = 5
tiwttersAgragados = 0
elementosNuevos = False
listaTiwtter = []

driver = webdriver.Chrome(executable_path=r"D:\DriverChrome\chromedriver.exe")
driver.maximize_window()
driver.get("https://twitter.com/AnaPao_LePew")

time.sleep(5)
#article
while tiwttersAgragados < numeroTiwtters:
    articulos = driver.find_elements_by_tag_name("article")

    # if tiwttersAgragados < numeroTiwtters:
    #     driver.execute_script("window.scrollTo(0, 500)") 
    
    if len(articulos)<numeroTiwtters+1:
        driver.execute_script("window.scrollTo(0, 500)") 
    else:
        for articulo in articulos:
            # print(articulo.text)
            textoPartido = articulo.text.split('\n')
            #Tweet fijado
            if 'Tweet fijado' not in textoPartido[0]:
                if tiwttersAgragados < numeroTiwtters:
                    tiwttersAgragados+=1
                    listaTiwtter +=[textoPartido]
                else:
                    break
    
for tiwtter in listaTiwtter:
    print(tiwtter)
        
driver.close()
# https://www.google.com/ 
msg = "Inicio de python"
array = ["1","2","3"]
print(array)
print(msg)