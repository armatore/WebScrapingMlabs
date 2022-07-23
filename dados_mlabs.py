from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
# from bs4 import BeautifulSoup
import csv
from dotenv import load_dotenv
import os
import sys

load_dotenv()
login = os.getenv('MLABS_EMAIL')
passwd = os.getenv('MLABS_PASSWD')

class ChromeAuto:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.service = Service('./chromedriver')
        self.options.add_argument('Perfil')
        self.chrome = webdriver.Chrome(
            service=self.service,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)
        self.chrome.maximize_window()

    def sair(self):
        self.chrome.quit()

    def clica_entrar(self):
        try:
            btn_entrar = self.chrome.find_element(By.CSS_SELECTOR, value='.sc-8b15f693-0')
            btn_entrar.click()

        except Exception as e:
            print(f'Erro ao clicar no entrar = {e}')

    def faz_login(self):
        try:
            input_login = self.chrome.find_element(By.CSS_SELECTOR, '#email')
            input_senha = self.chrome.find_element(By.CSS_SELECTOR, '#password')
            btn_entrar = self.chrome.find_element(By.CSS_SELECTOR, '#btnSubmit')
            input_login.send_keys(login)
            input_senha.send_keys(passwd)
            btn_entrar.click()

        except Exception as e:
            print(f'Erro ao fazer login - {e}')

    def relatorios_face(self):
        self.chrome.get('https://app.mlabs.com.br/monitoring/facebook')

    def dados_facebook(self):
        try:
            dados_face = []

            try:
                #LIKES DA PÁGINA
                like = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-0 > svg > g.highcharts-legend > g > g > g:nth-child(1) > text > tspan')
                like = like.text
                dados_face.append(like)
                deslike = self.chrome.find_element(By.CSS_SELECTOR, '#highcharts-0 > svg > g.highcharts-legend > g > g > g:nth-child(2) > text > tspan')
                deslike = deslike.text
                dados_face.append(deslike)
            except Exception:
                print('falha na coleta de likes da página')

            try:
                #PERFIL DOS FÃS
                total_fas_masc = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-4 > svg > g.highcharts-legend > g > g > g:nth-child(1) > text > tspan')
                total_fas_fem = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-4 > svg > g.highcharts-legend > g > g > g:nth-child(2) > text > tspan')
                p_eng_masc = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-4 > svg > g.highcharts-legend > g > g > g:nth-child(3) > text > tspan')
                p_eng_fem = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-4 > svg > g.highcharts-legend > g > g > g:nth-child(4) > text > tspan')
                total_fas_sem_gen = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-profiles > div:nth-child(1) > div > div > div > div.widgets.acpt-box-row > div:nth-child(1) > div > span.value')
                total_fas_eng_sem_gen = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-profiles > div:nth-child(1) > div > div > div > div.widgets.acpt-box-row > div:nth-child(2) > div > span.value')
                dados_face.append(total_fas_masc.text)
                dados_face.append(total_fas_fem.text)
                dados_face.append(p_eng_masc.text)
                dados_face.append(p_eng_fem.text)
                dados_face.append(f'Total de Fãs que não Informaram Genêro : {total_fas_sem_gen.text}')
                dados_face.append(f'Total de Pessoas Engajadas que não Informaram Genêro : {total_fas_eng_sem_gen.text}')
            except Exception:
                print('falha na coleta do perfil dos fãs')

            try:
                #Fãs Por Cidade
                tot_fas_cidade = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-6 > svg > g.highcharts-legend > g > g > g:nth-child(1) > text > tspan')
                pes_eng_cidade = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-6 > svg > g.highcharts-legend > g > g > g:nth-child(2) > text > tspan')
                dados_face.append(tot_fas_cidade.text)
                dados_face.append(pes_eng_cidade.text)
            except Exception:
                print('falha na coleta dos fãs por cidade')

            try:
                #Fãs por fonte
                outras_fontes = self.chrome.find_element(By.CLASS_NAME, value='acpt-box-table')
                dados_face.append(outras_fontes.text)
            except Exception:
                print('falha na coleta de fãs por fonte')

            try:
                # Efetividade da pagina
                alc_total = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(1) > text > tspan:nth-child(2)')
                dados_face.append(f'Alcance Total: {alc_total.text}')
                alc_pago = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(2) > text > tspan:nth-child(2)')
                dados_face.append(f'Alcance Pago: {alc_pago.text}')
                like_pag = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(3) > text > tspan:nth-child(2)')
                dados_face.append(f'Likes da Pagina: {like_pag.text}')
                alc_org = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(4) > text > tspan:nth-child(2)')
                dados_face.append(f'Alcance Organico: {alc_org.text}')
                user_env = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(5) > text > tspan:nth-child(2)')
                dados_face.append(f'Usuários envolvidos: {user_env.text}')
            except Exception:
                print('falha na coleta de efetivadade da página')

            try:
                #Interações
                i_curtir = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-10 > div > div > div > div:nth-child(1) > span > strong')
                i_amei = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-10 > div > div > div > div:nth-child(2) > span > strong')
                i_comentarios = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-10 > div > div > div > div:nth-child(3) > span > strong')
                i_click = self.chrome.find_element(By.CSS_SELECTOR,'#highcharts-10 > div > div > div > div:nth-child(4) > span > strong')
                dados_face.append(f'Curtir: {i_curtir.text}')
                dados_face.append(f'Amei: {i_amei.text}')
                dados_face.append(f'Comentarios: {i_comentarios.text}')
                dados_face.append(f'Click: {i_click.text}')
            except Exception:
                print('falha na coleta de interações')

            try:
                #Total de posts
                tot_posts = self.chrome.find_element(By.CSS_SELECTOR,'div.acpt-box-conteudo:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
                tot_interacoes = self.chrome.find_element(By.CSS_SELECTOR,'div.acpt-box-conteudo:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
                media_interacoes_post = self.chrome.find_element(By.CSS_SELECTOR,'div.acpt-box-conteudo:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
                dados_face.append(f'Total de Posts: {tot_posts.text}')
                dados_face.append(f'Total de interações: {tot_interacoes.text}')
                dados_face.append(f'Média de interações por Post: {media_interacoes_post.text}')
            except Exception:
                print('falha na coleta do Total de posts')

            try:
                #Melhor tipo de conteudo
                melhor_cont = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-contents > div:nth-child(2) > div > div > div.acpt-box-row > div > div.acpt-alert-content > div')
                dados_face.append(melhor_cont.text.replace('\n', ', '))
            except Exception:
                print('falha na coleta do melhor tipo de conteúdo')

            try:
                #Melhor periodo para postar
                print(f'melhor período para postar: ', end=' ')
                melhor_perio_post = self.chrome.find_element(By.CSS_SELECTOR,'.graph_52 > div:nth-child(2) > div:nth-child(1)')
                dados_face.append(melhor_perio_post.text.replace('\n', ', '))
            except Exception:
                print('Falha na coleta do melhor período para postar')

            for d in dados_face:
                print(d)

            #Html da pagina
            # pagina_html = self.chrome.find_element_by_css_selector('#acpt')
            # html = pagina_html.get_attribute('innerHTML')
            # soup = BeautifulSoup(html, 'html.parser')
            # print(soup.text)

            #salvando em csv
            with open('dados_csv/mlabs/dados_facebook.csv', 'w') as df:
                dados_faceb = csv.writer(df, delimiter=' ', quotechar='\n', quoting=csv.QUOTE_MINIMAL)
                dados_faceb.writerows([dados_face])

        except Exception as e:
            print('Erro: ', e)

    def relatorios_twitter(self):
        self.chrome.get('https://app.mlabs.com.br/monitoring/twitter')

    def dados_twitter(self):
        try:
            dados_tt = []

            try:
                #Total de seguidores
                tot_seguidores = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-header-content > div.acpt-header-text > div > h3')
                dados_tt.append(tot_seguidores.text.replace('\n', '   '))
            except Exception:
                print('falha na coleta do Total de seguidores')

            try:
                #Total de seguidores ganhos e perdidos
                seg_ganhos = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-followers > div:nth-child(1) > div > div > div > div.widgets.acpt-box-row > div:nth-child(1) > div:nth-child(1)')
                seg_perdidos = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-followers > div:nth-child(1) > div > div > div > div.widgets.acpt-box-row > div:nth-child(2) > div:nth-child(1)')
                dados_tt.append(seg_ganhos.text.replace('\n', '   '))
                dados_tt.append(seg_perdidos.text.replace('\n', '   '))
            except Exception:
                print('falha na coleta do Total de seguidores ganhos e perdidos')

            try:
                #Efetividade
                efe_post = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-effectiveness > div > div > div > div > div.effectiveness_header > div:nth-child(1)')
                eng_tot = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-effectiveness > div > div > div > div > div.effectiveness_header > div:nth-child(2)')
                pes_unicas = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-effectiveness > div > div > div > div > div.effectiveness_header > div:nth-child(3)')
                dados_tt.append(efe_post.text.replace("\n", "  "))
                dados_tt.append(eng_tot.text.replace("\n", "  "))
                dados_tt.append(pes_unicas.text.replace("\n", "  "))
            except Exception:
                print('falha na coleta da efetividade')

            try:
                #Influencia
                influencia = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-influences > div > div > div > div.influences_header')
                inf = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-influences > div > div > div > div.hashtags_graph.acpt-hashtags.influences_graph')
                dados_tt.append(influencia.text.replace("\n", "  "))
                dados_tt.append(inf.text.replace("\n", " | "))
            except Exception:
                print('falha na coleta de influencia')

            try:
                #Palavra-Chave
                pala_chaves = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-keywords > div > div > div > div.keywords_graph')
                dados_tt.append(pala_chaves.text.replace("\n", " | "))
            except Exception:
                print('falha na coleta da palavra-chave')

            try:
                #total de conteudos
                tot_conteudos = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-contents > div:nth-child(1) > div > div > div > div:nth-child(6)')
                dados_tt.append(tot_conteudos.text.replace('\n', '  '))
            except Exception:
                print('falha na coleta do total de conteúdo')

            try:
                #Melhor post
                mlhr_post_eng = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-contents > div:nth-child(1) > div > div > div > div:nth-child(4) > div')
                dados_tt.append(mlhr_post_eng.text.replace('\n', '  '))
            except Exception:
                print('falha na coleta do melhor post')

            try:
                #Melhor tipo de conteudo
                mlhr_tipo_cont = self.chrome.find_element(By.CSS_SELECTOR,'.graph_31 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > p:nth-child(2) > b:nth-child(1)')
                dados_tt.append(mlhr_tipo_cont.text.replace('\n', '  '))
            except Exception:
                print('falha na coleta do melhor tipo de conteúdo')

            try:
                #Melhor periodo para postagem
                mlhr_peri_post = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-contents > div:nth-child(3) > div > div > div.acpt-box-row > div')
                dados_tt.append(mlhr_peri_post.text.replace('\n', '  '))
            except Exception:
                print('falha na coleta do melhor período para postagem')

            for dt in dados_tt:
                print(dt)

            with open('dados_csv/mlabs/dados_twitter.csv', 'w', encoding='utf-8') as dtw:
                dados_tw = csv.writer(dtw, delimiter=' ', quotechar='\n', quoting=csv.QUOTE_MINIMAL)
                dados_tw.writerows([dados_tt])

        except Exception as e:
            print('Erro: ', e)

    def relatorios_insta(self):
        self.chrome.get('https://app.mlabs.com.br/monitoring/instagram')


    def dados_insta(self):
        try:

            try:
                data = self.chrome.find_element(By.XPATH, '//*[@id="acpt-periodo"]')
                print(data.get_attribute('value'), end='\n')

            except Exception:
                print('falha ao tentar alterar a data')

            dados_insta = []

            try:
                #Seguidores
                seguidores_insta = self.chrome.find_element(By.XPATH, '//*[@id="acpt-periodo"]')
                dados_insta.append(seguidores_insta.text.replace('\n', ' '))
            except Exception:
                print('erro na coleta de seguidores!' )

            try:
                #Melhor story
                mlhr_story_view = self.chrome.find_element(By.CSS_SELECTOR,'#acpt-box-stories > div:nth-child(1) > div > div > div > div:nth-child(4) > div')
                dados_insta.append(mlhr_story_view.text.replace('\n', ' '))
            except Exception:
                print('erro na coleta de melhor story!')

            try:
                # total storys
                tot_story = self.chrome.find_element(
                    By.CSS_SELECTOR,
                    '#acpt-box-stories > div:nth-child(1) > div > div > div > div:nth-child(6)')
                dados_insta.append(tot_story.text.replace('\n', ' '))
            except Exception:
                print('erro na coleta de total storys!')

            # Tabela
            # dr = self.chrome.find_element(
            #           By.CSS_SELECTOR,
            #           '#acpt-box-stories > div:nth-child(1) > div > div > div > div:nth-child(7) > header > table')
            # dados_insta.append(dr.text)

            try:
                # Melhor tipo de storys
                mlhr_tipo_story = self.chrome.find_element(
                    By.CSS_SELECTOR,
                    '#acpt-box-stories > div:nth-child(2) > div > div > div.acpt-box-row > div')
                dados_insta.append(mlhr_tipo_story.text.replace('\n', ' '))
            except Exception:
                print('erro na coleta do melhor tipo de story')

            try:
                # Melhor periodo para postagem
                mlhr_perio_post = self.chrome.find_element(
                    By.CSS_SELECTOR,
                    '.graph_52 > div:nth-child(2) > div:nth-child(1)')

                mlhr_hora_post = self.chrome.find_element(
                    By.CSS_SELECTOR,
                    '.graph_52 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2)')
                mlhr_perio_post = f'{mlhr_perio_post.text} | {mlhr_hora_post.text}'
                dados_insta.append(mlhr_perio_post.replace('\n', ' '))
            except Exception:
                print('erro na coleta de melhor período para postagem')

            try:
                #Genero dos seguidores
                gen_seg = self.chrome.find_element(
                    By.CSS_SELECTOR,
                    'g.highcharts-legend:nth-child(5)')
                dados_insta.append(gen_seg.text.replace('\n', ' '))
            except Exception:
                print('erro na coleta do melhor genero dos seguidores')

            try:
                #Total de posts
                tot_post = self.chrome.find_element(
                    By.CSS_SELECTOR,
                    '.graph_52 > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
                dados_insta.append(tot_post.text.replace('\n', '  '))
            except Exception:
                print('falha na coleta de total de posts')

            with open('dados_csv/mlabs/dados_instagram.csv', 'w', encoding='utf-8') as dtw:
                dados_ins = csv.writer(dtw, delimiter=' ', quotechar='\n', quoting=csv.QUOTE_MINIMAL)
                dados_ins.writerows([dados_insta])

            for di in dados_insta:
                print(di)

        except Exception as e:
            print(f'erro: {e}')


if __name__ == '__main__':
    wait_time = 2
    chrome = ChromeAuto()
    chrome.acessa('https://www.mlabs.com.br/')

    chrome.clica_entrar()
    sleep(wait_time)
    chrome.faz_login()
    sleep(wait_time)
    chrome.acessa('https://appsocial.mlabs.io/profiles/4630440/change_current_profile')
    sleep(wait_time)

    chrome.relatorios_face()
    sleep(wait_time)
    print('\nDados facebook')
    chrome.dados_facebook()

    sleep(wait_time)
    chrome.relatorios_twitter()
    sleep(wait_time)
    print('\nDados Twitter')
    chrome.dados_twitter()

    sleep(wait_time)
    chrome.relatorios_insta()
    sleep(wait_time)
    print('\nDados Instagram')
    chrome.dados_insta()

    chrome.sair()

