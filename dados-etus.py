from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import csv


class ChromeAuto:
    def __init__(self):
        self.drive_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('Perfil')
        self.chrome = webdriver.Chrome(
            self.drive_path,
            options=self.options
        )

    def acessa(self):
        self.chrome.get('https://front.etus.com.br/login')

    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_css_selector('#login')
            input_senha = self.chrome.find_element_by_css_selector('#content > section > section > form > div > div > div > div.login__row.spt > input')
            btn_entrar = self.chrome.find_element_by_css_selector('#content > section > section > form > div > div > div > button')

            input_login.send_keys('fleury@armatorems.com')
            sleep(1)
            input_senha.send_keys('sucesso2021@rede')
            sleep(1)
            btn_entrar.click()

        except Exception as e:
            print('Erro ao fazer login', e)

    def gerar_relatorio(self):
        self.chrome.get('https://front.etus.com.br/reports')

if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa()

    sleep(1)
    chrome.faz_login()
    sleep(5)
    chrome.gerar_relatorio()
