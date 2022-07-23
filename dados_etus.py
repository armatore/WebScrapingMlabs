import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import csv

from dotenv import load_dotenv
import os

load_dotenv()
login = os.getenv('ETUS_EMAIL')
passwd = os.getenv('ETUS_PASSWD')


class ChromeAuto:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.service = Service('./chromedriver')
        self.options.add_argument('Perfil')
        self.chrome = webdriver.Chrome(
            service=self.service,
            options=self.options
        )

    def acessa(self):
        self.chrome.get('https://front.etus.com.br/login')

    def sair(self):
        self.chrome.quit()

    #Digita os dados e faz o login
    def faz_login(self):
        try:
            input_login = self.chrome.find_element(By.CSS_SELECTOR,'#login')
            input_senha = self.chrome.find_element(By.CSS_SELECTOR,'#content > section > section > form > div > div > div > div.login__row.spt > input')
            btn_entrar = self.chrome.find_element(By.CSS_SELECTOR,'#content > section > section > form > div > div > div > button')

            input_login.send_keys(login)
            sleep(2)
            input_senha.send_keys(passwd)
            sleep(2)
            btn_entrar.click()

        except Exception as e:
            print('Erro ao fazer login', e)

    #Acessa pagina de Relatorios Emitidos
    def relatorios(self):
        self.chrome.get('https://front.etus.com.br/reports')

    #Copiar link do relatorio que vai extrair os dados
    def codigo_relatorio(self):
        self.chrome.get('https://report.etus.com.br/report/share/amFhWEpyOHVYSU0vZGlzeUJXOEIwVmk2WU5CclY1a2NTNm5wcXZ0cXZZbEZ1aVZtTzZGeXNaN0ZpV3dKTXdkdA==')

    def dados_face(self):
        dados_face = []

        #Likes da pagina
        like_pag_ini = self.chrome.find_element(By.CSS_SELECTOR,'#app-facebook > div:nth-child(2) > div > div.box-top-body.position-relative > div > div:nth-child(1) > div > b')
        like_pag_final = self.chrome.find_element(By.CSS_SELECTOR,'#app-facebook > div:nth-child(2) > div > div.box-top-body.position-relative > div > div:nth-child(2) > div > b')
        novos_likes = self.chrome.find_element(By.CSS_SELECTOR,'#app-facebook > div:nth-child(2) > div > div.box-top-body.position-relative > div > div:nth-child(3) > div > div > b')
        cres_likes = self.chrome.find_element(By.CSS_SELECTOR, '#app-facebook > div:nth-child(2) > div > div.box-top-body.position-relative > div > div:nth-child(4) > div > div > b')

        # Alcance total da pagina
        alc_tot_pag = self.chrome.find_element(By.CSS_SELECTOR, '#reach-page-paid-organic-facebook > div:nth-child(1) > div > div > b')
        alc_tot_org = self.chrome.find_element(By.CSS_SELECTOR, '#reach-page-paid-organic-facebook > div:nth-child(2) > div > div > b')

        #resultados das publicações
        num_posts = self.chrome.find_element(By.CSS_SELECTOR, '#posts-abstract-facebook > div.row.no-gutters > div:nth-child(1) > div > div > b')
        compartilhamento = self.chrome.find_element(By.CSS_SELECTOR, '#posts-abstract-facebook > div.row.no-gutters > div:nth-child(2) > div > div > b')
        comentarios = self.chrome.find_element(By.CSS_SELECTOR, '#posts-abstract-facebook > div.row.no-gutters > div:nth-child(3) > div > div > b')
        click = self.chrome.find_element(By.CSS_SELECTOR, '#posts-abstract-facebook > div.row.no-gutters > div:nth-child(4) > div > div > b')
        impressoes = self.chrome.find_element(By.CSS_SELECTOR, '#posts-abstract-facebook > div.row.no-gutters > div:nth-child(5) > div > div > b')
        reacoes = self.chrome.find_element(By.CSS_SELECTOR, '#posts-abstract-facebook > div.row.no-gutters > div:nth-child(6) > div > div > b')

        # Melhores horarios para postagem
        mlhr_hra_post = self.chrome.find_element(By.CSS_SELECTOR, '#app-facebook > div:nth-child(10) > div > div.box-top-body.position-relative > p')

        dados_facebook = {
            'likes_pagina': {
                    'like_pagina_inicial': like_pag_ini.text,
                    'like_pagina_final': like_pag_final.text,
                    'novas_curtidas': novos_likes.text,
                    'crescimento_likes': cres_likes.text
            },
            'alcance_total_pagina': {
                    'alcance_total_pago': alc_tot_pag.text,
                    'alcance_total_organico': alc_tot_org.text,
            },
            'resultado_das_publicacoes': {
                    'numero_postagens': num_posts.text,
                    'compartilhamentos': compartilhamento.text,
                    'comentarios': comentarios.text,
                    'cliques': click.text,
                    'impressoes': impressoes.text,
                    'reacoes': reacoes.text,
            },
            'melhor_hora_postagem': {
                'Mehor_hora_postar': mlhr_hra_post.text
            }
        }

        dados_face.append(dados_facebook)

        with open('dados_json/etus/dados_etus_facebook.json', 'w', encoding='utf-8') as dfe:
            json.dump(dados_face, dfe, ensure_ascii=False, indent=5, separators=(',', ':'))

        for df in dados_face:
            print(df)

    def relatorios_instagram(self):
        rel_insta = self.chrome.find_element(By.CSS_SELECTOR, '#report-vue > div > ul > li:nth-child(2) > a')
        rel_insta.click()

    def dados_instagram(self):
        dados_insta = []

        #Resumo Geral
        alc = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(2) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(1) > div > div > b')
        impres = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(2) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(2) > div > div > b')
        vis_perfil = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(2) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(3) > div > div > b')
        tot_click = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(2) > div > div.box-top-body.position-relative > div:nth-child(3) > div > div > div > b')

        # #Variacao de seguidores no periodo
        # variacao_seguidores = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(5) > div.col-md-9.mb-1.pr-0.padding-sm-left-0 > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(1) > div > div > b')
        # crescimento_seguidores = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(5) > div.col-md-9.mb-1.pr-0.padding-sm-left-0 > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(2) > div > div > b')
        # num_inicial_seguidores = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(5) > div.col-md-9.mb-1.pr-0.padding-sm-left-0 > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(1) > div > div > b')
        # num_final_seguidores = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(5) > div.col-md-9.mb-1.pr-0.padding-sm-left-0 > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(2) > div > div > b')

        #Cidades com maior alcance
        cidades = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(8) > div > div.box-top-body.position-relative > table')

        #Visão geral dos cliques
        tipo_click = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(9) > div > div.box-top-body.position-relative > table')

        #Resultado das publicações
        comentarios_posts = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(10) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(1) > div > div > b')
        likes_posts = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(10) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(2) > div > div > b')
        impressoes_posts = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(10) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(3) > div > div > b')
        posts_salvos = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(10) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(4) > div > div > b')
        alc_posts = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(10) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(1) > div > div > b')
        eng_posts = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(10) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(2) > div > div > b')
        tot_posts = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(10) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(3) > div > div > b')

        # #Melhor hora para postar
        # mlhr_hora_post = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(11) > div > div.box-top-body.position-relative > div > p')
        #
        # informacoes gerais dos stories
        click_voltar = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(1) > div > div > b')
        sair_stories = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(2) > div > div > b')
        click_frente = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(3) > div > div > b')
        alc_stories = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(1) > div > div > b')
        impressoes_stories = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(2) > div > div > b')
        resposta_stories = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(3) > div > div > b')
        total_stories = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(4) > div:nth-child(1) > div > div > b')
        media_impressoes = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(4) > div:nth-child(2) > div > div > b')
        media_alc = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(4) > div:nth-child(3) > div > div > b')
        resposta_enquetes = self.chrome.find_element(By.CSS_SELECTOR, '#app-instagram > div:nth-child(16) > div > div.box-top-body.position-relative > div:nth-child(4) > div.col-md-12 > div > div > b')

        dados_instagram = {
            'resumo_geral': {
                    'alcance': alc.text,
                    'impressoes': impres.text,
                    'visualizacoes_perfil': vis_perfil.text,
                    'total_cliques_perfil': tot_click.text,
            },
            # 'Variacao_seguidores_periodo': {
            #         # 'Variacao_seguidores': variacao_seguidores.text,
            #         # 'Crescimento_seguidores': crescimento_seguidores.text,
            #         # 'Num_inicial_seguidores': num_inicial_seguidores.text,
            #         # 'Num_final_seguidores': num_final_seguidores.text,
            # },
            'cidade_com_maior_alcance': {
                    'cidades': cidades.text
            },
            'visao_geral_cliques': {
                    'tipo_cliques': tipo_click.text
            },
            'resultado_publicacoes': {
                    'comentarios_posts': comentarios_posts.text,
                    'likes_posts': likes_posts.text,
                    'impressoes_posts': impressoes_posts.text,
                    'posts_salvos': posts_salvos.text,
                    'alcance_posts': alc_posts.text,
                    'engajamento_posts': eng_posts.text,
                    'total_posts': tot_posts.text,
            },
            # 'Melhores_hora/dia_postar': {
            #         'Melhor_hd_post': mlhr_hora_post.text
            # },
            'informacoes_gerais_stories': {
                    'cliques_voltar': click_voltar.text,
                    'sair_storie': sair_stories.text,
                    'cliques_frente': click_frente.text,
                    'alcance_storie': alc_stories.text,
                    'impressoes_storie': impressoes_stories.text,
                    'resposta_storie': resposta_stories.text,
                    'total_stories': total_stories.text,
                    'media_impressoes': media_impressoes.text,
                    'media_alcance': media_alc.text,
                    'resposta_enquete': resposta_enquetes.text,
            }
        }

        dados_insta.append(dados_instagram)

        for di in dados_insta:
            print(di)

        with open('dados_json/etus/dados_etus_instagram.json', 'w', encoding='utf-8') as dfe:
            json.dump(dados_insta, dfe, ensure_ascii=False, indent=5, separators=(',', ':'))



    def relatorios_twitter(self):
        rel_insta = self.chrome.find_element(By.CSS_SELECTOR, '#report-vue > div > ul > li:nth-child(3) > a')
        rel_insta.click()

    def dados_twitter(self):
        try:
            dados_tt = []

            #Resumo Geral
            total_tweets = self.chrome.find_element(By.CSS_SELECTOR, '#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(1) > div > div > b')
            total_likes = self.chrome.find_element(By.CSS_SELECTOR, '#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(2) > div > div > b')
            total_retweets = self.chrome.find_element(By.CSS_SELECTOR, '#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(3) > div > div > b')
            total_interacoes = self.chrome.find_element(By.CSS_SELECTOR, '#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(4) > div > div > b')
            media_int_tweets = self.chrome.find_element(By.CSS_SELECTOR, '#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(5) > div > div > b')

            #Melhor dia e horario para postar
            mlhr_hora_post = self.chrome.find_element(By.CSS_SELECTOR, '#app-twitter > div:nth-child(7) > div > div.box-top-body > p')

            dado_twitter = {
                'resumo_geral': {
                        'total_tweets': total_tweets.text,
                        'total_likes': total_likes.text,
                        'total_retweets': total_retweets.text,
                        'total_interacoes': total_interacoes.text,
                        'media_interacoes_tweets': media_int_tweets.text,
                },
                'melhores_horarios_postar': {
                        'melhor_dia/hora_posts': mlhr_hora_post.text
                }
            }

            dados_tt.append(dado_twitter)

            for dt in dados_tt:
                print(dt)

            with open('dados_json/etus/dados_etus_twitter.json', 'w', encoding='utf-8') as dte:
                json.dump(dados_tt, dte, ensure_ascii=False, indent=4, separators=(',', ':'))

        except Exception as e:
            print('Erro: ', e)


if __name__ == '__main__':
    wait_time = 6

    chrome = ChromeAuto()
    chrome.acessa()
    sleep(wait_time)
    chrome.faz_login()
    sleep(wait_time)
    chrome.relatorios()
    sleep(wait_time)
    chrome.codigo_relatorio()
    sleep(wait_time)
    print('Dados Facebook')
    chrome.dados_face()
    sleep(wait_time)
    chrome.relatorios_instagram()
    sleep(wait_time)
    print('')
    print('Dados Instagram')
    chrome.dados_instagram()
    sleep(wait_time)
    chrome.relatorios_twitter()
    sleep(wait_time)
    print('')
    print('Dados Twitter')
    chrome.dados_twitter()
    sleep(wait_time)
    chrome.sair()
