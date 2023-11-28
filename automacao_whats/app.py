import openpyxl
from urllib.parse import quote 
import webbrowser
from time import sleep
import os
import pyautogui

os.chdir('/home/viktor/Área de Trabalho/python/DevAprender/automacao_whats/')


webbrowser.open('https://web.whatsapp.com/')
sleep(5)
workbook = openpyxl.load_workbook('numero.xlsx')
paginaComNumeros= workbook['Planilha1']

for linha in paginaComNumeros.iter_rows(min_row=1):
    numero = linha[0].value
    menssagem = "Olá meu nome é Viktor, essa é uma automação "
    
    try:
        linkMessage= f"https://wa.me/{numero}?text={quote(menssagem)}"
        webbrowser.open(linkMessage)
        sleep(1)
        incio = pyautogui.locateCenterOnScreen('iniciarConversa.png')
        sleep(2)
        pyautogui.click(incio[0],incio[1])
        sleep(1)
        usar = pyautogui.locateCenterOnScreen('usarWhats.png')
        sleep(2)
        pyautogui.click(usar[0],usar[1])
        sleep(15)
        seta = pyautogui.locateCenterOnScreen('seta.png')
        sleep(2)
        pyautogui.click(seta[0],seta[1])
        sleep(2)
        pyautogui.hotkey('Ctrl','w')
        pyautogui.hotkey('Ctrl','w')
        sleep(2)
    except:
         print(f'não foi possivel enviar menssagem para o numero: {numero}')
         with open('erros.cvs','a',newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'{numero}')
