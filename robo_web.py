#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import threading
import pygetwindow as gw
from screeninfo import get_monitors


instancias_abertas = []


chrome_options = Options()
chrome_options.add_argument("--disable-notifications")  
chrome_options.add_argument("--disable-popup-blocking")  

# lista de controladora para cada monitor
controladoras_por_instancia = {
    #monitor 1
    0: ['//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[1]/a',
        '//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[2]/a',
       '//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[3]/a',
       '//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[4]/a',
       '//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[5]/a'],
    
    #monitor 2
    1: ['//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[6]/a',
        '//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[7]/a'],

    #monitor 3
    2: ['//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[8]/a',
        '//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[9]/a',
       '//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[10]/a'],

    #monitor
    3: ['//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[11]/a',
        '//*[@id="ui-id-1"]/div[1]/div[2]/div/div/div[2]/ul/li[12]/a'],
}


instancia_para_monitor = {
    0: 0,  
    1: 1,  
    2: 2, 
    3: 3, 
}

#reconhecimento dos monitores
def obter_posicoes_monitores():
    return [(monitor.x, monitor.y) for monitor in get_monitors()]

# Função para mover a janela para um monitor específico e maximizar
def mover_janela(navegador, instancia_id):
    time.sleep(3)  # Aguarda o navegador abrir completamente
    janelas = gw.getWindowsWithTitle("Google Chrome")
    if janelas:
        try:
            posicoes_monitores = obter_posicoes_monitores()
            monitor_id = instancia_para_monitor.get(instancia_id, 0)  # Padrão: Monitor 0
            if monitor_id < len(posicoes_monitores):
                x, y = posicoes_monitores[monitor_id]
                janela = janelas[-1]  # Última janela aberta
                janela.moveTo(x, y)
                janela.maximize()  # Maximiza a janela após mover
                navegador.fullscreen_window()  # Ativa o modo tela cheia (F11)
                print(f"Movendo instância {instancia_id} para monitor {monitor_id}: ({x}, {y})")
        except Exception as e:
            print(f"Erro ao mover a janela: {e}")

# Função para abrir uma instância do navegador e realizar ações específicas
def abrir_pagina_e_realizar_acoes(instancia_id):
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service, options=chrome_options)
    instancias_abertas.append(navegador)

    try:
        navegador.get("https://SITE.COM.BR")
        
        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="usuEmail"]'))
        ).send_keys('LOGIN')
        navegador.find_element(By.XPATH, '//*[@id="usuPassword"]').send_keys('SENHA')
        navegador.find_element(By.XPATH, '//*[@id="login"]').click()

        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[1]/div[2]/div[1]/button'))
        ).click()

        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ui-id-1"]/div[1]/div[2]/div/button'))
        ).click()

        for xpath in controladoras_por_instancia[instancia_id]:
            WebDriverWait(navegador, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            ).click()
            time.sleep(1)

        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ui-id-1"]/button[1]/span[2]'))
        ).click()
        
        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ui-id-1"]/button[2]'))
        ).click()

        # Move a instância para um monitor específico e maximiza
        mover_janela(navegador, instancia_id)

        print(f"Instância {instancia_id} configurada com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro na instância {instancia_id}: {e}")

# numero de pag que abrirão
numero_de_instancias = min(4, len(get_monitors()))  

threads = []
for i in range(numero_de_instancias):
    thread = threading.Thread(target=abrir_pagina_e_realizar_acoes, args=(i,))
    threads.append(thread)
    thread.start()
    time.sleep(2)



