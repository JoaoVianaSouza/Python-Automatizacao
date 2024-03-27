# Passo 1: Acessar o chrome e entrar no site https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer o "login" (digitar algo no campo de email e senha)
# Passo 3: Importar base de dados
# Passo 4: Cadastrar os produtos em looping até todos serem cadastrados

import pyautogui #biblioteca responsável pelas ações (automações)
import time
import pandas as pd #biblioteca para trabalhar com analise de dados

pyautogui.PAUSE = 0.5 

#Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")

#Digitar a URL
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

#Logar no site
pyautogui.click(x=804, y=391)
pyautogui.write("Teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("testeteste")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("enter")

#Trabalhar a base de dados com a biblioteca 'pandas'    
table = pd.read_csv('produtos.csv')
#Cadastrar os produtos (looping)
for line in table.index:
    pyautogui.click(x=892, y=258)
    pyautogui.write(str(table.loc[line, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(table.loc[line, "custo"])) 
    pyautogui.press("tab")
    obs = table.loc[line, "obs"]
    if not pd.isna(obs): #Se tiver algo escrito no obs
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll(5000) #Subir a tela para repetir o processo
    


    