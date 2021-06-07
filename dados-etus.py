import json

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

    def relatorios(self):
        self.chrome.get('https://front.etus.com.br/reports')

    def codigo_relatorio(self):
        self.chrome.get('https://report.etus.com.br/report/share/amFhWEpyOHVYSU0vZGlzeUJXOEIwVmk2WU5CclY1a2NTNm5wcXZ0cXZZbUprUDUySHFzSEs5eW1Yc0F0V0NDZQ==')

    def dados_face(self):
        dados_face = []

        #Likes da pagina
        like_pag_ini = self.chrome.find_element_by_css_selector('#app-facebook > div:nth-child(2) > div > div.box-top-body.position-relative > div > div:nth-child(1) > div > b')
        like_pag_final = self.chrome.find_element_by_css_selector('#app-facebook > div:nth-child(2) > div > div.box-top-body.position-relative > div > div:nth-child(2) > div > b')
        novos_likes = self.chrome.find_element_by_css_selector('#app-facebook > div:nth-child(2) > div > div.box-top-body.position-relative > div > div:nth-child(3) > div > div > b')
        cres_likes = self.chrome.find_element_by_css_selector('#app-facebook > div:nth-child(2) > div > div.box-top-body.position-relative > div > div:nth-child(4) > div > div > b')

        # Alcance total da pagina
        alc_tot_pag = self.chrome.find_element_by_css_selector('#reach-page-paid-organic-facebook > div:nth-child(1) > div > div > b')
        alc_tot_org = self.chrome.find_element_by_css_selector('#reach-page-paid-organic-facebook > div:nth-child(2) > div > div > b')

        #resultados das publicações
        num_posts = self.chrome.find_element_by_css_selector('#posts-abstract-facebook > div.row.no-gutters > div:nth-child(1) > div > div > b')
        compartilhamento = self.chrome.find_element_by_css_selector('#posts-abstract-facebook > div.row.no-gutters > div:nth-child(2) > div > div > b')
        comentarios = self.chrome.find_element_by_css_selector('#posts-abstract-facebook > div.row.no-gutters > div:nth-child(3) > div > div > b')
        click = self.chrome.find_element_by_css_selector('#posts-abstract-facebook > div.row.no-gutters > div:nth-child(4) > div > div > b')
        impressoes = self.chrome.find_element_by_css_selector('#posts-abstract-facebook > div.row.no-gutters > div:nth-child(5) > div > div > b')
        reacoes = self.chrome.find_element_by_css_selector('#posts-abstract-facebook > div.row.no-gutters > div:nth-child(6) > div > div > b')

        # Melhores horarios para postagem
        mlhr_hra_post = self.chrome.find_element_by_css_selector('#app-facebook > div:nth-child(10) > div > div.box-top-body.position-relative > p')

        dados_facebook = {
            'Likes_pagina': {
                    'Like_pagina_inicial': like_pag_ini.text,
                    'Like_pagina_final': like_pag_final.text,
                    'Novas_curtidas': novos_likes.text,
                    'Crescimento_likes': cres_likes.text
            },
            'Alcance_total_pagina': {
                    'Alcance_total_pago': alc_tot_pag.text,
                    'Alcance_total_organico': alc_tot_org.text,
            },
            'Resultado_das_publicacoes': {
                    'Numero_postagens': num_posts.text,
                    'Compartilhamentos': compartilhamento.text,
                    'Comentarios': comentarios.text,
                    'Cliques': click.text,
                    'Impressoes': impressoes.text,
                    'Reacoes': reacoes.text,
            },
            'Melhor_hora_postagem': {
                'Mehor_hora_postar': mlhr_hra_post.text
            }
        }

        dados_face.append(dados_facebook)

        with open('dados_etus_facebook.json', 'w', encoding='utf-8') as dfe:
            json.dump(dados_face, dfe, ensure_ascii=False, sort_keys=True, indent=5, separators=(',', ':'))

        for df in dados_face:
            print(df)

    def relatorios_instagram(self):
        rel_insta = self.chrome.find_element_by_css_selector('#report-vue > div > ul > li:nth-child(2) > a')
        rel_insta.click()

    def dados_instagram(self):
        try:
            dados_insta = []

            #Resumo Geral
            alc = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(2) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(1) > div > div > b')
            impres = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(2) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(2) > div > div > b')
            vis_perfil = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(2) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(3) > div > div > b')
            tot_click = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(2) > div > div.box-top-body.position-relative > div:nth-child(3) > div > div > div > b')

            #Variacao de seguidores no periodo
            variacao_seguidores = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(5) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(1) > div > div > b')
            crescimento_seguidores = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(5) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(2) > div > div > b')
            num_inicial_seguidores = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(5) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(1) > div > div > b')
            num_final_seguidores = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(5) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(2) > div > div > b')

            #Cidades com maior alcance
            cidades = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(8) > div > div.box-top-body.position-relative > div > div:nth-child(1) > table')

            #Visão geral dos cliques
            tipo_click = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(8) > div > div.box-top-body.position-relative > div > div:nth-child(2) > table')

            #Resultado das publicações
            comentarios_posts = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(9) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(1) > div > div > b')
            likes_posts = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(9) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(2) > div > div > b')
            impressoes_posts = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(9) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(3) > div > div > b')
            posts_salvos = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(9) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(4) > div > div > b')
            alc_posts = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(9) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(1) > div > div > b')
            eng_posts = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(9) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(2) > div > div > b')
            tot_posts = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(9) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(3) > div > div > b')

            #Melhor hora para postar
            mlhr_hora_post = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(11) > div > div.box-top-body.position-relative > div > p')

            # informacoes gerais dos stories
            click_voltar = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(1) > div > div > b')
            sair_stories = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(2) > div > div > b')
            click_frente = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(2) > div:nth-child(3) > div > div > b')
            alc_stories = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(1) > div > div > b')
            impressoes_stories = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(2) > div > div > b')
            resposta_stories = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(3) > div:nth-child(3) > div > div > b')
            total_stories = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(4) > div:nth-child(1) > div > div > b')
            media_impressoes = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(4) > div:nth-child(2) > div > div > b')
            media_alc = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(4) > div:nth-child(3) > div > div > b')
            resposta_enquetes = self.chrome.find_element_by_css_selector('#app-instagram > div:nth-child(13) > div > div.box-top-body.position-relative > div:nth-child(4) > div.col-md-12 > div > div > b')

            dados_instagram = {
                'Resumo_geral': {
                        'Alcance': alc.text,
                        'Impressoes': impres.text,
                        'Visualizacoes_perfil': vis_perfil.text,
                        'Total_cliques_perfil': tot_click.text,
                },
                'Variacao_seguidores_periodo': {
                        'Variacao_seguidores': variacao_seguidores.text,
                        'Crescimento_seguidores': crescimento_seguidores.text,
                        'Num_inicial_seguidores': num_inicial_seguidores.text,
                        'Num_final_seguidores': num_final_seguidores.text,
                },
                'Cidade_com_maior_alcance': {
                        'cidades': cidades.text.replace('\n', ' | ')
                },
                'Visão_geral_cliques': {
                        'tipo_cliques': tipo_click.text.replace('\n', ' | ')
                },
                'Resultado_publicacoes': {
                        'Comentarios_posts': comentarios_posts.text,
                        'Likes_posts': likes_posts.text,
                        'Impressoes_posts': impressoes_posts.text,
                        'Posts_salvos': posts_salvos.text,
                        'Alcance_posts': alc_posts.text,
                        'Engajamento_posts': eng_posts.text,
                        'total_posts': tot_posts.text,
                },
                'Melhores_hora/dia_postar': {
                        'Melhor_hd_post': mlhr_hora_post.text
                },
                'Informacoes_gerais_stories': {
                        'Cliques_voltar': click_voltar.text,
                        'Sair_storie': sair_stories.text,
                        'Cliques_frente': click_frente.text,
                        'Alcance_storie': alc_stories.text,
                        'Impressoes_storie': impressoes_stories.text,
                        'Resposta_storie': resposta_stories.text,
                        'Total_stories': total_stories.text,
                        'Media_impressoes': media_impressoes.text,
                        'Media_alcance': media_alc.text,
                        'Resposta_enquete': resposta_enquetes.text,
                }
            }

            dados_insta.append(dados_instagram)

            for di in dados_insta:
                print(di)

            with open('dados_etus_instagram.json', 'w', encoding='utf-8') as dfe:
                json.dump(dados_insta, dfe, ensure_ascii=False, sort_keys=True, indent=5, separators=(',', ':'))

        except Exception as e:
            print('Erro: ', e)

    def relatorios_twitter(self):
        rel_insta = self.chrome.find_element_by_css_selector('#report-vue > div > ul > li:nth-child(3) > a')
        rel_insta.click()

    def dados_twitter(self):
        try:
            dados_tt = []

            #Resumo Geral
            total_tweets = self.chrome.find_element_by_css_selector('#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(1) > div > div > b')
            total_likes = self.chrome.find_element_by_css_selector('#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(2) > div > div > b')
            total_retweets = self.chrome.find_element_by_css_selector('#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(3) > div > div > b')
            total_interacoes = self.chrome.find_element_by_css_selector('#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(4) > div > div > b')
            media_int_tweets = self.chrome.find_element_by_css_selector('#app-twitter > div:nth-child(2) > div > div.box-top-body > div > div:nth-child(5) > div > div > b')

            #Melhor dia e horario para postar
            mlhr_hora_post = self.chrome.find_element_by_css_selector('#app-twitter > div:nth-child(7) > div > div.box-top-body > p')

            dado_twitter = {
                'Resumo Geral': {
                        'Total_tweets': total_tweets.text,
                        'Total_likes': total_likes.text,
                        'Total_retweets': total_retweets.text,
                        'Total_interacoes': total_interacoes.text,
                        'Media_interacoes_tweets': media_int_tweets.text,
                },
                'Melhores horarios postar': {
                        'Melhor_dia/hora_posts': mlhr_hora_post.text
                }
            }

            dados_tt.append(dado_twitter)

            for dt in dados_tt:
                print(dt)

            with open('dados_etus_twitter.json', 'w', encoding='utf-8') as dte:
                json.dump(dados_tt, dte, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))

        except Exception as e:
            print('Erro: ', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa()
    sleep(1)
    chrome.faz_login()
    sleep(5)
    chrome.relatorios()
    sleep(1)
    chrome.codigo_relatorio()
    sleep(2)
    print('Dados Facebook')
    chrome.dados_face()
    sleep(5)
    chrome.relatorios_instagram()
    sleep(4)
    print('')
    print('Dados Instagram')
    chrome.dados_instagram()
    sleep(4)
    chrome.relatorios_twitter()
    sleep(4)
    print('')
    print('Dados Twitter')
    chrome.dados_twitter()
    sleep(20)
    chrome.sair()
