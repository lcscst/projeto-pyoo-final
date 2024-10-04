import os
from validar_url import validar_url

class NavegadorWebSimulado:

    def __init__(self, arquivo_urls):
        self.paginas = {
            "www.ifpb.edu.br": ["/tsi", "/rc"],
            "www.ifpb.edu.br/tsi": ["/professores", "/alunos"],
            "www.ifpb.edu.br/rc": ["/coordenacao"],
            "www.ifpb.edu.br/rc/coordenacao": ["/matriz_curricular"],
            "www.google.com.br": ["/search", "/images"],
            "www.apple.com": ["/iphone", "/mac"],
            "www.detran.pb.gov.br": ["/servicos", "/contato"],
        }
        self.historico_navegacao = []
        self.historico_completo = []
        self.home = ""
        self.url_atual = ""

        self.urls_invalidas = []

        diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
        caminho_completo_arquivo = os.path.join(diretorio_do_script, arquivo_urls)

        self.carregar_urls_validas(caminho_completo_arquivo)

    def carregar_urls_validas(self, caminho_completo_arquivo):
        try:
            with open(caminho_completo_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    url = linha.strip()
                    if validar_url(url):
                        if url not in self.paginas:
                            self.paginas[url] = []
                    else:
                        self.urls_invalidas.append(url)
        except FileNotFoundError:
            print(f"\nErro: Arquivo '{caminho_completo_arquivo}' não encontrado.")
        except Exception as e:
            print(f"\nOcorreu um erro ao carregar URLs: {e}")

    def navegar_para(self, url):
        try:
            if url.startswith("/"):
                if self.url_atual and url in self.paginas.get(self.url_atual, []):
                    self.historico_navegacao.append(self.url_atual)
                    self.historico_completo.append(self.url_atual)
                    self.url_atual += url
                elif self.home and url in self.paginas.get(self.home, []):
                    self.historico_navegacao.append(self.url_atual)
                    self.historico_completo.append(self.url_atual)
                    self.url_atual = self.home + url
                else:
                    print("\nPágina não encontrada!")
                    return
            
            elif url in self.paginas:
                if self.url_atual:
                    self.historico_navegacao.append(self.url_atual)
                    self.historico_completo.append(self.url_atual)
                self.url_atual = url
                self.home = url
            else:
                print("\nPágina não encontrada!")
                return
            
            self.exibir_links_disponiveis()
        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {str(e)}")

    def exibir_links_disponiveis(self):
        print(f"\nPágina encontrada: {self.url_atual}\n")
        print("Links disponíveis:")
        links = self.paginas.get(self.url_atual, [])
        if links:
            for link in links:
                print(f"  {link}")
        else:
            print("Nenhum link disponível.")

    def executar_comando(self, comando):
        try:
            if comando.startswith("#add "):
                url = comando.split(" ")[1]
                if validar_url(url):
                    if url not in self.paginas:
                        self.paginas[url] = []
                        print(f"\n{url} adicionado com sucesso!")
                    else:
                        print("\nA URL já existe no sistema.")
                else:
                    print("\nFormato de URL inválido!\nExemplo de formato válido: www.url.com")
            elif comando == "#back":
                if self.historico_navegacao:
                    self.url_atual = self.historico_navegacao.pop()
                    self.exibir_links_disponiveis()
                else:
                    print("\nNão há páginas anteriores.")
            elif comando == "#sair":
                print("\nFechando o navegador...\n")
                return False
            elif comando == "#showhist":
                print(f"\nHistórico completo:\n{self.historico_completo}")
            elif comando == "#help":
                self.exibir_ajuda()
            elif comando == "#showurls":
                print("\nURLs válidas no sistema:")
                for url in self.paginas.keys():
                    print(f"  {url}")
                print("\nURLs inválidas:")
                if self.urls_invalidas:
                    for url in self.urls_invalidas:
                        print(f"  {url}")
                else:
                    print("  Nenhuma URL inválida foi encontrada.")
            else:
                print("\nComando inválido.")
        except Exception as e:
            print(f"\nOcorreu um erro ao executar o comando: {str(e)}")
        return True

    def exibir_ajuda(self):
        print("\nComandos disponíveis no navegador:")
        print("#add <url> -- Adicionar uma nova URL")
        print("#back -- Voltar para a página anterior")
        print("#showhist -- Mostrar o histórico completo de navegação")
        print("#showurls -- Mostrar as URLs")
        print("#sair -- Fechar o navegador")

    def exibir_urls_carregadas(self):
        print("\nURLs carregadas no sistema:")
        for url in self.paginas.keys():
            print(f"  {url}")