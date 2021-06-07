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
            sleep(1)
            input_senha.send_keys('sucesso2021@rede')
            sleep(1)
            btn_entrar.click()

        except Exception as e:
            print('Erro ao fazer login')

    def relatorios_face(self):
        self.chrome.get('https://app.mlabs.com.br/monitoring/facebook')

    def dados_facebook(self):
        dados_face = []

        # LIKES DA PÁGINA
        like = self.chrome.find_element_by_css_selector('#highcharts-0 > svg > g.highcharts-legend > g > g > g:nth-child(1) > text > tspan')
        deslike = self.chrome.find_element_by_css_selector('#highcharts-0 > svg > g.highcharts-legend > g > g > g:nth-child(2) > text > tspan')

        # PERFIL DOS FÃS
        total_fas_masc = self.chrome.find_element_by_css_selector('#highcharts-4 > svg > g.highcharts-legend > g > g > g:nth-child(1) > text > tspan')
        total_fas_fem = self.chrome.find_element_by_css_selector('#highcharts-4 > svg > g.highcharts-legend > g > g > g:nth-child(2) > text > tspan')
        p_eng_masc = self.chrome.find_element_by_css_selector('#highcharts-4 > svg > g.highcharts-legend > g > g > g:nth-child(3) > text > tspan')
        p_eng_fem = self.chrome.find_element_by_css_selector('#highcharts-4 > svg > g.highcharts-legend > g > g > g:nth-child(4) > text > tspan')
        total_fas_sem_gen = self.chrome.find_element_by_css_selector('#acpt-box-profiles > div:nth-child(1) > div > div > div > div.widgets.acpt-box-row > div:nth-child(1) > div > span.value')
        total_fas_eng_sem_gen = self.chrome.find_element_by_css_selector('#acpt-box-profiles > div:nth-child(1) > div > div > div > div.widgets.acpt-box-row > div:nth-child(2) > div > span.value')

        # Fãs Por Cidade
        tot_fas_cidade = self.chrome.find_element_by_css_selector('#highcharts-6 > svg > g.highcharts-legend > g > g > g:nth-child(1) > text > tspan')
        pes_eng_cidade = self.chrome.find_element_by_css_selector('#highcharts-6 > svg > g.highcharts-legend > g > g > g:nth-child(2) > text > tspan')

        # Fãs por fonte
        outras_fontes = self.chrome.find_element_by_class_name('acpt-box-table')

        # Efetividade da pagina
        alc_total = self.chrome.find_element_by_css_selector('#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(1) > text > tspan:nth-child(2)')
        alc_pago = self.chrome.find_element_by_css_selector('#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(2) > text > tspan:nth-child(2)')
        like_pag = self.chrome.find_element_by_css_selector('#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(3) > text > tspan:nth-child(2)')
        alc_org = self.chrome.find_element_by_css_selector('#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(4) > text > tspan:nth-child(2)')
        user_env = self.chrome.find_element_by_css_selector('#highcharts-8 > svg > g.highcharts-legend > g > g > g:nth-child(5) > text > tspan:nth-child(2)')

        # Interações
        i_curtir = self.chrome.find_element_by_css_selector('#highcharts-10 > div > div > div > div:nth-child(1) > span > strong')
        i_amei = self.chrome.find_element_by_css_selector('#highcharts-10 > div > div > div > div:nth-child(2) > span > strong')
        i_comentarios = self.chrome.find_element_by_css_selector('#highcharts-10 > div > div > div > div:nth-child(3) > span > strong')
        i_click = self.chrome.find_element_by_css_selector('#highcharts-10 > div > div > div > div:nth-child(4) > span > strong')

        # Total de posts
        tot_posts = self.chrome.find_element_by_css_selector('#acpt-box-contents > div:nth-child(1) > div > div > div > div:nth-child(6) > div:nth-child(1) > div > div > span')
        tot_interacoes = self.chrome.find_element_by_css_selector('#acpt-box-contents > div:nth-child(1) > div > div > div > div:nth-child(6) > div:nth-child(2) > div > div > span')
        media_interacoes_post = self.chrome.find_element_by_css_selector('#acpt-box-contents > div:nth-child(1) > div > div > div > div:nth-child(6) > div:nth-child(3) > div > div > span')

        # Melhor tipo de conteudo
        melhor_cont = self.chrome.find_element_by_css_selector('#acpt-box-contents > div:nth-child(2) > div > div > div.acpt-box-row > div > div.acpt-alert-content > div')

        # Melhor periodo para postar
        melhor_perio_post = self.chrome.find_element_by_css_selector('#acpt-box-contents > div:nth-child(3) > div > div > div.acpt-box-row > div')

        dados_facebk = {
                'Likes_pagina': {
                        'Total_likes': like.text,
                        'Total_deslikes': deslike.text,
                },
                'Perfil_fas': {
                        'Total_fas_masc': total_fas_masc.text,
                        'Total_fas_fem': total_fas_fem,
                        'Pessoas_engajadas_masc': p_eng_masc.text,
                        'Pessoas_engajadas_fem': p_eng_fem.text,
                        'Total_fas_sem_genero': total_fas_sem_gen.text,
                        'Total_fas_eng_sem_genero': total_fas_eng_sem_gen.text,
                },
                'Fas_por_cidade': {
                        'total_fas_cidade': tot_fas_cidade.text,
                        'Pessoas_eng_cidade': pes_eng_cidade.text,
                },
                'Fas_por_fonte': {
                        'Outras_fontes': outras_fontes.text
                },
                'Efetividade_pagina': {
                        'Alcance_total': alc_total.text,
                        'Alcance_pago': alc_pago.text,
                        'Likes_pagina': like_pag.text,
                        'Alcance_organico': alc_org.text,
                        'Usuários_envolvidos': user_env.text,
                },
                'Interacoes': {
                        'Curtir': i_curtir.text,
                        'Amei': i_amei.text,
                        'Comentarios': i_comentarios.text,
                        'Click': i_click.text,
                },
                'Total_posts': {
                        'Total_post': tot_posts.text,
                        'Total_interacoes': tot_interacoes.text,
                        'Media_interacoes_por_post': media_interacoes_post.text,
                },
                'Melhor_tipo_conteudo': {
                        'Melhor_conteudo': melhor_cont.text
                },
                'Melhor_periodo_postar': {
                        'Melhor_dia/hora_postar': melhor_perio_post.text
                },
        }

        dados_face.append(dados_facebk)

        with open('dados_mlabs_facebook.json', 'w', encoding='utf-8') as dfe:
            json.dump(dados_face, dfe, ensure_ascii=False, sort_keys=True, indent=5, separators=(',', ':'))

        for df in dados_face:
            print(df)

    def relatorios_twitter(self):
        self.chrome.get('https://app.mlabs.com.br/monitoring/twitter')

    def dados_twitter(self):
        dados_tt = []

        # Total de seguidores
        tot_seguidores = self.chrome.find_element_by_css_selector('#acpt-header-content > div.acpt-header-text > div > h3')

        # Total de seguidores ganhos e perdidos
        seg_ganhos = self.chrome.find_element_by_css_selector('#acpt-box-followers > div:nth-child(1) > div > div > div > div.widgets.acpt-box-row > div:nth-child(1) > div:nth-child(1)')
        seg_perdidos = self.chrome.find_element_by_css_selector('#acpt-box-followers > div:nth-child(1) > div > div > div > div.widgets.acpt-box-row > div:nth-child(2) > div:nth-child(1)')

        # Efetividade
        efe_post = self.chrome.find_element_by_css_selector('#acpt-box-effectiveness > div > div > div > div > div.effectiveness_header > div:nth-child(1)')
        eng_tot = self.chrome.find_element_by_css_selector('#acpt-box-effectiveness > div > div > div > div > div.effectiveness_header > div:nth-child(2)')
        pes_unicas = self.chrome.find_element_by_css_selector('#acpt-box-effectiveness > div > div > div > div > div.effectiveness_header > div:nth-child(3)')

        # Influencia
        influencia = self.chrome.find_element_by_css_selector('#acpt-box-influences > div > div > div > div.influences_header')
        inf = self.chrome.find_element_by_css_selector('#acpt-box-influences > div > div > div > div.hashtags_graph.acpt-hashtags.influences_graph')

        # Palavra-Chave
        pala_chaves = self.chrome.find_element_by_css_selector('#acpt-box-keywords > div > div > div > div.keywords_graph')

        # total de conteudos
        tot_conteudos = self.chrome.find_element_by_css_selector('#acpt-box-contents > div:nth-child(1) > div > div > div > div:nth-child(6)')

        # Melhor post
        mlhr_post_eng = self.chrome.find_element_by_css_selector('#acpt-box-contents > div:nth-child(1) > div > div > div > div:nth-child(4) > div')

        # Melhor tipo de conteudo
        mlhr_tipo_cont = self.chrome.find_element_by_css_selector('#acpt-box-contents > div:nth-child(2) > div > div > div.acpt-box-row > div')

        # Melhor periodo para postagem
        mlhr_peri_post = self.chrome.find_element_by_css_selector('#acpt-box-contents > div:nth-child(3) > div > div > div.acpt-box-row > div')

        dados_twitter = {
            'Total_seguidores': {
                    'Total_seguidores': tot_seguidores.text,
            },
            'Total_seguidores_ganhos_perdidos': {
                    'Seguidores_ganhos': seg_ganhos.text,
                    'Seguidores_perdidos': seg_perdidos.text,
            },
            'Efetividade': {
                    'Efetividade_posts': efe_post.text,
                    'Total_engajamento': eng_tot.text,
                    'Pessoas_unicas': pes_unicas.text,
            },
            'Influencia': {
                    'Influencia': influencia.text,
                    'Influenciadores': inf.text
            },
            'Palavra_chave': {
                    'Palavras_chaves': pala_chaves.text
            },
            'Total_conteudos': {
                    'total_conteudos': tot_conteudos.text
            },
            'Melhor_posts': {
                    'Melhor_post_eng': mlhr_post_eng.text
            },
            'Melhor_tipo_conteudo': {
                    'Melhor_tipo_conteudos': mlhr_tipo_cont.text
            },
            'Melhor_periodo_post': {
                    'Melhor_dia/hora_postar': mlhr_peri_post
            }

        }

        dados_tt.append(dados_twitter)

        with open('dados_mlabs_facebook.json', 'w', encoding='utf-8') as dtm:
            json.dump(dados_tt, dtm, ensure_ascii=False, sort_keys=True, indent=5, separators=(',', ':'))

        for dt in dados_tt:
            print(dt)

    def relatorios_insta(self):
        self.chrome.get('https://app.mlabs.com.br/monitoring/instagram')

    def dados_insta(self):
        dados_insta = []

        # Seguidores
        seguidores_insta = self.chrome.find_element_by_css_selector('#acpt-header-content > div.acpt-header-text > div')

        # Melhor story
        mlhr_story_view = self.chrome.find_element_by_css_selector('#acpt-box-stories > div:nth-child(1) > div > div > div > div:nth-child(4) > div')

        # total storys
        tot_story = self.chrome.find_element_by_css_selector('#acpt-box-stories > div:nth-child(1) > div > div > div > div:nth-child(6)')

        # Melhor tipo de storys
        mlhr_tipo_story = self.chrome.find_element_by_css_selector('#acpt-box-stories > div:nth-child(2) > div > div > div.acpt-box-row > div')

        # Melhor periodo para postagem
        mlhr_perio_post = self.chrome.find_element_by_css_selector('#acpt-box-stories > div:nth-child(5) > div > div > div.acpt-box-row > div')

        # Genero dos seguidores
        gen_seg = self.chrome.find_element_by_css_selector('#highcharts-10 > svg > g.highcharts-legend')

        # Total de posts
        tot_post = self.chrome.find_element_by_css_selector('#acpt-box-posts > div:nth-child(1) > div > div > div > div:nth-child(6)')

        dados_instagram = {
            'Seguidores': {
                'total_seguidores': seguidores_insta.text,
            },
            'Melhor_storie': {
                'Melhor_story_por_view': mlhr_story_view.text
            },
            'Total_stories': {
                'Total_stories': tot_story.text
            },
            'Melhor_tipo_storie': {
                'Melhor_tipo_story': mlhr_tipo_story.text
            },
            'Melhor_periodo_post': {
                'Melhor_perio_postar': mlhr_perio_post.text
            },
            'Genero_seguidores': {
                'Genero_dos_seguidores': gen_seg.text
            },
            'Total_posts': {
                'Total_postagens': tot_post.text
            }

        }
        dados_insta.append(dados_instagram)

        for di in dados_insta:
            print(di)

        with open('dados_etus_instagram.json', 'w', encoding='utf-8') as dim:
            json.dump(dados_insta, dim, ensure_ascii=False, sort_keys=True, indent=5, separators=(',', ':'))


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://www.mlabs.com.br/')

    chrome.clica_entrar()
    sleep(1)
    chrome.faz_login()

    sleep(3)
    chrome.relatorios_face()
    sleep(2)
    print('Dados facebook')
    chrome.dados_facebook()

    sleep(5)
    chrome.relatorios_twitter()
    sleep(3)
    print('')
    print('Dados Twitter')
    chrome.dados_twitter()

    sleep(5)
    chrome.relatorios_insta()
    sleep(3)
    print('')
    print('Dados Instagram')
    chrome.dados_insta()
