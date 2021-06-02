from selenium import webdriver
from time import sleep


class ChromeAuto:
    def __init__(self):
        self.drive_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('Perfil')
        self.chrome = webdriver.Chrome(
            self.drive_path,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()


    def clica_entrar(self):
        try:
            btn_entrar = self.chrome.find_element_by_class_name('menu-login')
            btn_entrar.click()
        except Exception as e:
            print('Erro ao clicar no entrar')


    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('email')
            input_senha = self.chrome.find_element_by_id('password')
            btn_entrar = self.chrome.find_element_by_id('btnSubmit')

            input_login.send_keys('fleury00@gmail.com')
            input_senha.send_keys('sucesso2021@rede')
            sleep(2)
            btn_entrar.click()
        except Exception as e:
            print('Erro ao fazer login'
                  '')



if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://www.mlabs.com.br/')

    chrome.clica_entrar()
    chrome.faz_login()

    sleep(15)
    chrome.sair()
