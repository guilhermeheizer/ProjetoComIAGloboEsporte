from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Importação do webdriver-manager
import time
from gerador_html import gerar_tabela_html

class CampeonatoBrasileiroScraper:
    def __init__(self):
        # Configurações do WebDriver usando webdriver-manager
        self.chrome_options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)

        # Dicionários para armazenar os dados
        self.tabela_brasileirao = {}
        self.time_escudo = {}

    def navegar_para_site(self, url="https://ge.globo.com/futebol/brasileirao-serie-b/?_ga=2.112892996.1193706931.1766090285-883144322.1718917913"):
                          # url="https://ge.globo.com/futebol/brasileirao-serie-a/"):
        """Navega para o site do Campeonato Brasileiro."""
        self.driver.get(url)
        time.sleep(5)  # Aguarda a página carregar completamente

    def obter_rodada_atual(self):
        """Obtém a rodada atual carregada por padrão no site."""
        rodada_element = self.driver.find_element(By.XPATH, '//span[contains(@class, "lista-jogos__navegacao--rodada")]')
        rodada_texto = rodada_element.text.strip().split("ª")[0]  # Exemplo: "3ª RODADA" -> "3"
        return int(rodada_texto)

    def carregar_dados_rodada(self, rodada):
        """Carrega os dados de uma rodada e salva no dicionário tabela_brasileirao."""
        print(f"Carregando dados da rodada {rodada}...")

        # Localiza os 10 jogos da rodada
        jogos = self.driver.find_elements(By.XPATH, '//li[contains(@class, "lista-jogos__jogo")]')
        rodada_dados = []

        for jogo in jogos:
            try:
                # Extrai as informações do jogo
                local = jogo.find_element(By.XPATH, './/span[contains(@class, "jogo__informacoes--local")]').text.strip() or "NULO"
                data = jogo.find_element(By.XPATH, './/span[contains(@class, "jogo__informacoes--data")]').text.strip()
                hora = jogo.find_element(By.XPATH, './/span[contains(@class, "jogo__informacoes--hora")]').text.strip() or "NULO"

                placar_box = jogo.find_element(By.XPATH, './/div[contains(@class, "placar-box")]')
                time_mandante_placar = placar_box.find_element(By.XPATH, './/span[contains(@class, "placar-box__valor--mandante")]').text.strip() or "NULO"
                time_visitante_placar = placar_box.find_element(By.XPATH, './/span[contains(@class, "placar-box__valor--visitante")]').text.strip() or "NULO"

                time_mandante = jogo.find_element(By.XPATH, './/div[contains(@class, "placar__equipes--mandante")]')
                time_mandante_sigla = time_mandante.find_element(By.XPATH, './/span[contains(@class, "equipes__sigla")]').text.strip()
                time_mandante_nome = time_mandante.find_element(By.XPATH, './meta[@itemprop="name"]').get_attribute("content")
                                                     
                time_visitante = jogo.find_element(By.XPATH, './/div[contains(@class, "placar__equipes--visitante")]')
                time_visitante_sigla = time_visitante.find_element(By.XPATH, './/span[contains(@class, "equipes__sigla")]').text.strip()
                time_visitante_nome = time_visitante.find_element(By.XPATH, './meta[@itemprop="name"]').get_attribute("content")

                # Adiciona o dicionário do jogo à lista da rodada
                rodada_dados.append({
                    "local": local,
                    "data": data,
                    "hora": hora,
                    "time_mandante_sigla": time_mandante_sigla,
                    "time_mandante_nome": time_mandante_nome,
                    "placar_time_mandante": time_mandante_placar,
                    "time_visitante_sigla": time_visitante_sigla,
                    "time_visitante_nome": time_visitante_nome,
                    "placar_time_visitante": time_visitante_placar,
                })

                # Adiciona os escudos ao dicionário time_escudo (se ainda não estiverem salvos)
                if time_mandante_sigla not in self.time_escudo:
                    escudo_mandante = time_mandante.find_element(By.XPATH, './/img[contains(@class, "equipes__escudo")]').get_attribute("src")
                    self.time_escudo[time_mandante_sigla] = escudo_mandante

                if time_visitante_sigla not in self.time_escudo:
                    escudo_visitante = time_visitante.find_element(By.XPATH, './/img[contains(@class, "equipes__escudo")]').get_attribute("src")
                    self.time_escudo[time_visitante_sigla] = escudo_visitante

            except Exception as e:
                print(f"Erro ao coletar dados de um jogo: {e}")

        # Salva os dados da rodada no dicionário principal
        self.tabela_brasileirao[str(rodada)] = rodada_dados

    def navega_rodada(self, direcao):
        """Navega entre rodadas."""
        if direcao == "C":
            seta = self.driver.find_element(By.XPATH, '//span[contains(@class, "lista-jogos__navegacao--seta-direita")]')
        elif direcao == "D":
            seta = self.driver.find_element(By.XPATH, '//span[contains(@class, "lista-jogos__navegacao--seta-esquerda")]')

        seta.click()
        time.sleep(5)  # Aguarda o carregamento da nova rodada

    def executar(self):
        """Fluxo principal do programa."""
        self.navegar_para_site()

        # Obtém a rodada atual e solicita o tipo de navegação
        rodada_atual = self.obter_rodada_atual()
        crescente_decrescente = input("Carregar as rodadas crescente ou decrescente (C ou D): ").upper()

        if crescente_decrescente not in ["C", "D"]:
            print("Opção inválida. Use 'C' para crescente ou 'D' para decrescente.")
            return

        # Define o intervalo de rodadas com base na escolha
        if crescente_decrescente == "C":
            rodadas = range(rodada_atual, 39)
        else:
            rodadas = range(rodada_atual, 0, -1)

        # Itera sobre as rodadas
        for rodada in rodadas:
            self.carregar_dados_rodada(rodada)

            # Finaliza o loop se atingir os limites
            if (crescente_decrescente == "C" and rodada == 38) or (crescente_decrescente == "D" and rodada == 1):
                break
            else:
                self.navega_rodada(crescente_decrescente)

        # Encerra o navegador
        self.driver.quit()

        # Mostra os resultados
        # print("Tabela do Campeonato Brasileiro:")
        # print(self.tabela_brasileirao)
        # print("\nEscudos dos Times:")
        # print(self.time_escudo)
        # Gera o HTML

        tabela_brasileirao_ordenada = {
    rodada: jogos for rodada, jogos in sorted(self.tabela_brasileirao.items(), key=lambda item: int(item[0]))
}
        html = gerar_tabela_html(tabela_brasileirao_ordenada, self.time_escudo)

        # Salva o HTML em um arquivo
        with open("tabela_brasileirao.html", "w", encoding="utf-8") as arquivo:
            arquivo.write(html)

        print("Arquivo HTML gerado com sucesso!")

if __name__ == "__main__":
    scraper = CampeonatoBrasileiroScraper()
    scraper.executar()